#!/usr/local/bin/python3

"""Shower Thoughts

Usage:
  shower_thoughts
  shower_thoughts update
  shower_thoughts open
  shower_thoughts config

Options:
  -h --help     Show this screen.
"""

from docopt import docopt
import lib

class ShowerThoughts():


    def __init__(self, args):

        self.config = lib.Config()

        self.connection = lib.Reddit(self.config)

        # description='Displays a random shower thought from reddit',
           #          usage='''shower_thought <command> [<args>]
           #
           # update       Update local database of shower thoughts
           # open         Open comments section of last quote
           # conf         Get or set setting in config file''')

        if args['update']:
            self.update()

    def read(self):
        try:
            self.connection.read()
        except Exception:
            print("Unable to read database.  Try running \"shower_thoughts update\"")

    def update(self):
        self.connection.pull()
        print("Updated")

    def conf(self):
        import pprint
        pp = pprint.PrettyPrinter()
        pp.pprint(self.config.get())


    def open(self):
        import os
        if os.path.exists(self.config.configDir + '/lastDisplayed.json'):
            with open(self.config.configDir + '/lastDisplayed.json', 'r') as last:
                import json
                x = json.loads(last.read())
                import webbrowser
                webbrowser.open(x['permalink'], new=0, autoraise=True)


        with open(self.configDir + '/config.json', 'r') as configFile:
            self.config = json.loads(configFile.read())


if __name__ == '__main__':

    arguments = docopt(__doc__, version='Shower Thoughts')
    print(arguments)
    ShowerThoughts(arguments)

