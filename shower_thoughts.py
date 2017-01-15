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
           open         Open comments section of last quote
           config       Get or set config''')

        parser.add_argument('command',
            help='Subcommand to run [update|config|open]',
            nargs='?', default="")

        parser.parse_args()
        args = parser.parse_args(sys.argv[1:2])

        # default response
        if args.command == "":
            self.read()
            print(self.connection.randomThought())
            exit(1)

        # valid response
        elif args.command in ['update','config','open']:
            if args.command == 'update':
                self.update()
            elif args.command == 'open':
                self.open()
            elif args.command == 'config':
                self.configSet()



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

    def update(self):
        self.connection.pull()


    def configSet(self):
        parser2 = argparse.ArgumentParser(
            description='Set config options'
        )
        parser2.add_argument('--timeframe')
        parser2.add_argument('--limit', type=int)
        parser2.add_argument('--subreddit')
        parser2.add_argument('--section')
        parser2.parse_args()
        args = parser2.parse_args(sys.argv[3:])
        print(args)
        print('Timeframe set to {}'.format(args.limit))


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