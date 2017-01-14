import sys
import os

class Config():

	def __init__(self):

		# create config folder
		from os.path import expanduser
		home = os.path.expanduser("~")
		if not os.path.exists(home+'/.config/shower_thoughts'):
			print("First run: creating config folder in ~/.config/shower_thoughts")
			os.mkdir(home+'/.config/shower_thoughts')

		if not os.path.exists(home+'/.config/shower_thoughts/config.json'):
			print("No config file: copying from example file")
			# copy example config file
			from shutil import copyfile
			copyfile('config.json.example', home+'/.config/shower_thoughts/config.json')