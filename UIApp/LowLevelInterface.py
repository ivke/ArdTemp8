#!/usr/bin/python

import time
from threading import Thread
from ArduinoControl import *

class SerialWorker:
	isRunning = False

	def __init__(self, tempReadingCallback, serialReadingCallback):
		self.tempReadingCallback = tempReadingCallback
		self.serialReadingCallback = serialReadingCallback
		self.ArdTemp=TempControler()
	def start(self):
		t = Thread(target=self._serialWorkerThread)
		t.start()

	def handleSetTemperature(self, id, value):
		print 'Sending to serial: ' + str(id) + ': ' + str(value)
		if self.ArdTemp.SetTemp(int(id), int(value)) is None:
			pass
	
		# put code for sending temp to serial port
		#TempControl.SetTempForArduino(id, value)

	def _serialWorkerThread(self):
		self.isRunning = True
		while self.isRunning:

			## put code for reading from serial port in here
			# tempsDict, rawSerial = TempControl.GetTempFromArduino
			## assuming that tempsDict has sensor ids as keys
			# for sensorId in tempsDict:
			#	temp = tempsDict[key]
			#	self.tempReadingCallback(sensorId, temp)
			# self.serialReadingCallback(rawSerial)

			# sample - just to see something showing up in the screen
			self.ArdTemp.GetTempDict()   
			for key,value in self.ArdTemp.TempDict.items():
				self.tempReadingCallback(key, value)
			
			self.serialReadingCallback("This is raw serial")
			time.sleep(5)
			
	
	def stop(self):
		self.isRunning = False

	
