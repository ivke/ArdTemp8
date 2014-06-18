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

	def _serialWorkerThread(self):
		self.isRunning = True
		while self.isRunning:			
			self.ArdTemp.GetTempDict()   			
			
			for key,value in self.ArdTemp.TempDict.items():	# self.ArdTemp.TempDict => key=sensor id; value=temperature
				self.tempReadingCallback(key, value)			
			self.serialReadingCallback(self.ArdTemp.lastSerialReading)
			
			time.sleep(5)
			
	
	def stop(self):
		self.isRunning = False

	
