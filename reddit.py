import gzip
import json
import requests
from thought import Thought

class Reddit:


	def pull(self, timeframe="all", limit="100"):

		url = "https://www.reddit.com/r/showerthoughts/top.json?t={}&limit={}".format(timeframe, limit)

		output = requests.get(url).json()

		with open('database.json', 'w') as database:
			json.dump(output, database)


	def read(self):

		with open('database.json', 'r') as database:
			data = json.loads(database.read())

		thoughts = []

		data2 = data['data']['children']
		for x in data2:
			thoughts.append(Thought(x['data']))

		for x in thoughts:
			print(x,"\n")