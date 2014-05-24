#!/usr/bin/python
#
# Before running, pyqt4 must be installed.
# sudo apt-get install python-qt4 
# sudo yum install PyQt4
#

import sys
from PyQt4 import QtGui
from Calibration import ReadCalibratedSet
from UserInterface import MainWindow
from UserInterface import UIUpdater
from LowLevelInterface import SerialWorker

class MainApp:
	def __init__(self):
		self.app = QtGui.QApplication(sys.argv)
		self.app.aboutToQuit.connect(self.stop)

		# hook up UI window, UI updater and backend interface
		self.mainWindow = MainWindow()
		self.uiUpdater = UIUpdater(self.mainWindow.handleTempSignal, self.mainWindow.handleRawSerialSignal)
		self.serialWorker = SerialWorker(self.uiUpdater.raiseTemperatureEvent, self.uiUpdater.raiseRawSerialEvent)
		self.mainWindow.setTemperatureHandler(self.serialWorker.handleSetTemperature)
		ReadCalibratedSet()
		
	def addTemperatureSensor(self, id, unit):
		self.mainWindow.addTempSensor(id, unit)

	def addTemperatureControl(self, id, unit):
		self.mainWindow.addTempControl(id, unit)
	
	def start(self):

		self.mainWindow.start()
		self.uiUpdater.start()
		self.serialWorker.start()

		sys.exit(self.app.exec_())

	def stop(self):
		self.uiUpdater.stop()
		self.serialWorker.stop()

def main():
	app = MainApp()
	# add 8 temperature sensors with ids 1..8 and unit of Celsius
	app.addTemperatureSensor(1, 'C')	
	app.addTemperatureSensor(2, 'C')
	app.addTemperatureSensor(3, 'C')
	app.addTemperatureSensor(4, 'C')
	app.addTemperatureSensor(5, 'C')
	app.addTemperatureSensor(6, 'C')
	app.addTemperatureSensor(7, 'C')
	app.addTemperatureSensor(8, 'C')
	# add 3 temperature controls with ids 1..3 and unit of Celsius
	app.addTemperatureControl(1, 'C')
	app.addTemperatureControl(2, 'C')
	app.addTemperatureControl(3, 'C')
	app.start()

if __name__ == '__main__':
	main()
