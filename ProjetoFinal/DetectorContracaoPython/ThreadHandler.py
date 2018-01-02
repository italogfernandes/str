# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# FEDERAL UNIVERSITY OF UBERLANDIA
# Faculty of Electrical Engineering
# Biomedical Engineering Lab
#------------------------------------------------------------------------------
# Author: Andrei Nakagawa, MSc
# Contact: nakagawa.andrei@gmail.com
# Class: ThreadHander
# Modifications: Italo G S Fernandes
# 				(italogsfernandes@gmail.com, github.com/italogfernandes)
#------------------------------------------------------------------------------
# Description:
#------------------------------------------------------------------------------
from threading import Thread
#------------------------------------------------------------------------------
class ThreadHandler():
	def __init__(self,_worker=None):
		self.thread = Thread(target=self.run)
		self.worker = _worker
		self.isAlive = False
		self.isPaused = False
		self.flagRun = True
		self.flagPause = True

	def start(self):
		if self.isAlive == False:
			self.thread.start()
			self.isAlive = True
			self.flagPause = False

	def pause(self):
		if(self.isAlive & self.isPaused == False):
			self.flagPause = True
			self.isPaused = True

	def resume(self):
		if(self.isAlive and self.isPaused):
			self.flagPause = False
			self.isPaused = False

	def stop(self):
		if(self.isAlive):
			self.flagPause = True
			self.flagRun = False
		self.thread = Thread(target=self.run)
		self.isAlive = False
		self.isPaused = False
		self.flagRun = True
		self.flagPause = True

	def run(self):
		while self.flagRun:
			while self.flagPause is False:
				if self.worker is not None:
					self.worker()

if __name__ == "__main__":

	#This example demonstrates how to use the ThreadHandler class
	#for reading user input

	th = []

	def work():
		global th
		print 'waiting....'
		raw_input()
		print 'gotcha!'
		print 'killing thread'
		th.kill()
		print 'terminated'

	th = ThreadHandler(work)
	th.start()
