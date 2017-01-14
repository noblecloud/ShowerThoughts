import gzip
import json
import requests
from lib import thought
from random import choice

class Reddit():


	def pull(self, timeframe="all", limit="100"):

		url = "https://www.reddit.com/r/showerthoughts/top.json?t={}&limit={}".format(timeframe, limit)

		output = requests.get(url).json()

		with open('database.json', 'w') as database:
			json.dump(output, database)


	def read(self):

		with open('database.json', 'r') as database:
			data = json.loads(database.read())

		self.thoughts = []

		data = data['data']['children']
		for x in data:
			self.thoughts.append(thought.Thought(x['data']))

	def randomThought(self):
		thought = choice(self.thoughts)
		return thought