#!/usr/local/bin/python3

from lib import config
from lib import thought
from lib import reddit
import sys


class ShowerThoughts():


    def __init__(self):

        self.config = config.Config()

        self.connection = reddit.Reddit(self.config)

        # description='Displays a random shower thought from reddit',
                    usage='''shower_thought <command> [<args>]

           update       Update local database of shower thoughts
           open         Open comments section of last quote
           conf         Get or set setting in config file''')

        # parser.add_argument('command',
            help='Subcommand to run [update|conf|open]', nargs='*')

    def read(self):
        try:
            self.connection.read()
        except Exception:
            self.connection.pull()
            self.read()

    def update(self):
        self.connection.pull()


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


        # with open(self.configDir + '/config.json', 'r') as configFile:
        #     self.config = json.loads(configFile.read())



if __name__ == '__main__':
    ShowerThoughts()