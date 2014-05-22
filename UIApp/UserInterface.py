#!/usr/bin/python

import Queue
import threading
import datetime
from PyQt4 import QtGui, QtCore

class TempOutWidget:
	def __init__(self, sensorId, unit):
		self.id = sensorId
		self.label = QtGui.QLabel('Temp ' + str(sensorId) + ' [' + unit + ']:')
	
		self.txtTemp = QtGui.QLineEdit()
		self.txtTemp.setReadOnly(True)
		self.txtTemp.setFixedWidth(60)

		self.txtTimestamp = QtGui.QLineEdit()
		self.txtTimestamp.setReadOnly(True)
		self.txtTimestamp.setFixedWidth(200)

class TempInWidget:
	def __init__(self, sensorId, unit, tempHandler):
		self.id = sensorId
		self.tempHandler = tempHandler

		self.label = QtGui.QLabel('Set temp ' + str(sensorId) + ' [' + unit + ']:')
		
		self.txtTemp = QtGui.QLineEdit()
		self.txtTemp.setFixedWidth(60)
		self.btnSetTemp = QtGui.QPushButton('Set')
		self.btnSetTemp.setFixedWidth(60)
		self.btnSetTemp.clicked.connect(self._handleButton)
		self.normalBtnBorder = self.btnSetTemp.styleSheet()	

	def _handleButton(self):
		temp = str(self.txtTemp.text())

		print 'Sensor ' + str(self.id) + ' clicked with ' + temp

		if not temp.isdigit():
			self.txtTemp.setStyleSheet('border: 2px solid red;')
		else:
			self.txtTemp.setStyleSheet(self.normalBtnBorder)
			if not self.tempHandler is None:
				self.tempHandler(self.id, temp)
	

class MainWindow(QtGui.QWidget):
	def __init__(self):
		self.tempSensorWidgets = []
		self.tempControlWidgets = []
		self.tempHandler = None

		self.lblDescription = QtGui.QLabel('This is a super duper temperature reader. Readings from sensors, temp controls, etc..')
		self.lblDescription.setWordWrap(True)

		self.lblRawSerial = QtGui.QLabel('Raw serial reading log:')
		self.valRawSerial = QtGui.QTextEdit()
		self.valRawSerial.setReadOnly(True)

		super(MainWindow, self).__init__()		

	def addTempSensor(self, id, unit):
		self.tempSensorWidgets.append(TempOutWidget(id, unit))

	def addTempControl(self, id, unit):
		self.tempControlWidgets.append(TempInWidget(id, unit, self.tempHandler))

	def setTemperatureHandler(self, handler):
		self.tempHandler = handler

	def start(self):
		self._initUI()

	def _initUI(self):

		grid = QtGui.QGridLayout()
		grid.setSpacing(10)
		
		grid.addWidget(self.lblDescription, 0, 0, 1, 2)
	
		rowNum = 1
		for i in range(0, len(self.tempSensorWidgets)):
			tempWidget = self.tempSensorWidgets[i]
			grid.addWidget(tempWidget.label, rowNum, 0)
			grid.addWidget(tempWidget.txtTemp, rowNum, 1)
			grid.addWidget(tempWidget.txtTimestamp, rowNum, 2)
			rowNum += 1
		for i in range(0, len(self.tempControlWidgets)):
			tempWidget = self.tempControlWidgets[i]
			grid.addWidget(tempWidget.label, rowNum, 0)
			grid.addWidget(tempWidget.txtTemp, rowNum, 1)
			grid.addWidget(tempWidget.btnSetTemp, rowNum, 2)
			rowNum += 1
		grid.addWidget(self.lblRawSerial, rowNum+1, 0)
		grid.addWidget(self.valRawSerial, rowNum+2, 0, 5, 3)

		self.setLayout(grid)

		self.setMinimumSize(500, 800)
		self.resize(500, 800)
		self.center()

		self.setWindowTitle('Super duper temperature reader')
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	def handleTempSignal(self, sensorId, temp, timestamp):
		print 'New temp UI event:\n'
		print '..sensor = ' + str(sensorId)
		print '..temp = ' + str(temp)
		print '..timestamp = ' + str(timestamp)

		tempTxt = None
		timestampTxt = None
		self.tempSensorWidgets

		sensorWidget = next((x for x in self.tempSensorWidgets if x.id == sensorId), None)
		if not sensorWidget is None:
			sensorWidget.txtTemp.setText(str(temp))
			sensorWidget.txtTimestamp.setText(timestamp)
		else:
			print 'Widget with temp sensor ' + str(sensorId) + ' not found'

	def handleRawSerialSignal(self, raw, timestamp):
		print 'New serial reading UI event:\n'
		print '..raw = ' + str(raw)
		print '..timestamp = ' + str(timestamp)

		log = timestamp + ": " + raw + "\n" + self.valRawSerial.toPlainText()
		self.valRawSerial.setText(log)

class GenericEvent:
	def __init__(self, timestamp):
		self.timestamp = timestamp

class StopEvent(GenericEvent):
	def __init__(self):
		GenericEvent.__init__(self, datetime.datetime.utcnow())
	

class TemperatureReadingEvent(GenericEvent):
	def __init__(self, sensorId, val, timestamp):
		self.sensorId = sensorId
		self.val = val
		GenericEvent.__init__(self, timestamp)
		
class SerialReadingEvent(GenericEvent):
	def __init__(self, val, timestamp):
		self.val = val
		self.timestamp = timestamp
		GenericEvent.__init__(self, timestamp)

class UIUpdater(QtCore.QThread):
	# temp signal - 1st int = id of temp sensor, 2nd int = temp, 3rd str = timestamp
	tempSignal = QtCore.pyqtSignal(int, int, str)
	# serial signal - 1st str = rawserial, 2nd str = timestamp
	serialSignal = QtCore.pyqtSignal(str, str)
	
	isRunning = False
	eventsQueue = Queue.Queue()

	def __init__(self, tempSignalHandler, serialSignalHandler, parent=None):
		super(UIUpdater, self).__init__()

		self.tempSignal.connect(tempSignalHandler)
		self.serialSignal.connect(serialSignalHandler)

	def raiseTemperatureEvent(self, sensorId, val):
		self.eventsQueue.put(TemperatureReadingEvent(sensorId, val, str(datetime.datetime.utcnow())))	

	def raiseRawSerialEvent(self, raw):
		self.eventsQueue.put(SerialReadingEvent(raw, str(datetime.datetime.utcnow())))

	def stop(self):
		self.isRunning = False
		self.eventsQueue.put(StopEvent())
	
	def run(self):
		self.isRunning = True
		while self.isRunning:	
			toProcess = self.eventsQueue.get()
			# check for stop event
			if isinstance(toProcess, StopEvent):
				break

			if isinstance(toProcess, TemperatureReadingEvent):
				self.tempSignal.emit(toProcess.sensorId, toProcess.val, toProcess.timestamp)
			elif isinstance(toProcess, SerialReadingEvent):
				self.serialSignal.emit(toProcess.val, toProcess.timestamp)
			else:
				print "unknown event: " + str(type(toProcess))

			self.eventsQueue.task_done()


