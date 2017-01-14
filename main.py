#!/usr/local/bin/python3

from lib import config
from lib import thought
from lib import reddit
import argparse
import sys


class ShowerThoughts():


	def __init__(self):

		self.config = config.Config()

		self.connection = reddit.Reddit(self.config)

		parser = argparse.ArgumentParser(

		description='Displays a random shower thought from reddit',
					usage='''shower_thought <command> [<args>]

		   update       Update local database of shower thoughts
		   upvote       Upvote last displayed quote (must be logged in)
		   downvote     Downvote last disolayed quote (must be logged in)
		   open         Open comments section of last quote
		   config       Get or set config''')

		parser.add_argument('command',
			help='Subcommand to run [update|upvote|downvote|config|open]',
			nargs='?', default="")

		parser.parse_args()
		args = parser.parse_args(sys.argv[1:2])

		# default response
		if args.command == "":
			self.read()
			print(self.connection.randomThought())
			exit(1)

		# valid response
		elif args.command in ['update','upvote','downvote','config','open']:
			print("doing...")
			print(args.command)
			exit(1)

		# invalid response
		else:
			print('Unrecognized command')
			parser.print_help()
			exit(1)

	def read(self):
		try:
			self.connection.read()
		except Exception:
			self.connection.pull()
			self.read()

if __name__ == '__main__':
	ShowerThoughts()