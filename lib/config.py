import sys
import os
import json
import pickle

class Config():

	def __init__(self):

		# create config folder
		from os.path import expanduser
		self.configDir = os.path.expanduser("~") + '/.config/shower_thoughts'
		if not os.path.exists(self.configDir):
			print("First run: creating config folder in {}".format(self.configDir))
			os.mkdir(self.configDir)

		# copy example config file
		if not os.path.exists(self.configDir + '/config.json'):
			print("No config file: copying from example file")
			from shutil import copyfile
			copyfile('config.json.example', self.configDir + '/config.json')

		self.load()

	def load(self):
		with open(self.configDir + '/config.json', 'r') as configFile:
			self.config = json.loads(configFile.read())

		self.timeframe = self.config['config']['timeframe']
		self.limit = self.config['config']['limit']