import gzip
import json
import requests
from lib import thought
from random import choice
import pickle
import os

class Reddit():

	def __init__(self, configObj):
		self.config = configObj
		self.configDir = os.path.expanduser("~") + '/.config/shower_thoughts'


	def pull(self):

		url = "https://www.reddit.com/r/showerthoughts/top.json?t={}&limit={}".format(self.config.timeframe, self.config.limit)

		output = requests.get(url).json()

		if 'error' in output.keys():
			print(output['message'])

		else:
			if os.path.exists(self.configDir):
				with open(self.configDir + '/database.json', 'w') as database:
					json.dump(output, database)


	def read(self):
		if os.path.exists(self.configDir + '/database.json'):
			with open(self.configDir + '/database.json', 'r') as database:
				data = json.loads(database.read())

			self.thoughts = []

			data = data['data']['children']
			for x in data:
				self.thoughts.append(thought.Thought(x['data']))
		else:
			raise Exception("No database to pull from, run 'shower_thoughts update' first to pull from reddit.")


	def randomThought(self):
		thought = choice(self.thoughts)

		if os.path.exists(self.configDir):
			with open(self.configDir + '/lastDisplayed.json', 'w') as last:
				json.dump(thought.jsonExport(), last)

		return thought