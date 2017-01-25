#!/usr/local/bin/python3

"""Shower Thoughts

Usage:
  shower_thoughts
  shower_thoughts update
  shower_thoughts open
  shower_thoughts config (section|limit|timeframe|subreddit) [<value>]

Options:
  -h --help     Show this screen.
  update        pull latest data from reddit
  open          open comments page of last displayed item
  config        set or display a setting
"""

from docopt import docopt
import lib

class ShowerThoughts():


    def __init__(self, args):

        self.config = lib.Config()

        self.connection = lib.Reddit(self.config)

        value = args['<value>']
        if args['update']:
            self.update()
        elif args['open']:
            self.open()
        elif args['config']:

            if args['limit']:
                if value:
                    value = int(value)
                    if value <= 1 and value >= 100:
                        self.config.set('limit', value)
                    else:
                        print("Value for limit must be between 1 and 100")
                else:
                    print(self.config.get('limit'))

            if args['section']:
                if not value:
                    print(self.config.get('section'))
                else:
                    sections = ['hot', 'new', 'random', 'rising', 'top ', 'controversial']
                    if value in sections:
                        self.config.set('section', value)
                        print("Section set to {}".format(self.config.get('section')))
                    else:
                        print("Section must be hot, new, random, rising, top, controversial")

            if args['timeframe']:
                if not value:
                    print(self.config.get('timeframe'))
                else:
                    timeframes = ['hour', 'day', 'week', 'month', 'year', 'all']
                    if value in timeframes:
                        self.config.set('timeframe', value)
                        print("Timeframe set to {}".format(self.config.get('timeframe')))
                    else:
                        print("Timeframe must be hour, day, week, month, year, or all.")

            if args['subreddit']:
                if not value:
                    print(self.config.get('subreddit'))
                else:
                    self.config.set('subreddit', value)
                    print("Subreddi set to /r/{}".format(self.config.get('subreddit')))


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

