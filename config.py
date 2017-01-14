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