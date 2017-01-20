import sys
import os
import json
import pickle

class Config():


    def __init__(self):

        # create config folder
        from os.path import expanduser
        self.configDir = os.path.expanduser("~") + '/.config/shower_thoughts'
        if not os.path.exists(self.configDir):
            print("First run: creating config folder in {}".format(self.configDir))
            os.mkdir(self.configDir)

        # copy example config file
        if not os.path.exists(self.configDir + '/config.json'):
            print("No config file: copying from example file")
            from shutil import copyfile
            copyfile('config.json.example', self.configDir + '/config.json')

        self.load()


    def load(self):
        with open(self.configDir + '/config.json', 'r') as configFile:
            self.config = json.loads(configFile.read())

        # Reddit config
        self.timeframe = self.config['reddit']['timeframe']
        self.limit = self.config['reddit']['limit']
        self.subreddit = self.config['reddit']['subreddit']
        self.section = self.config['reddit']['section']

        # Display Config
        self.author = self.config['display']['author']
        self.score = self.config['display']['score']


    def save(self):

        # Reddit Config
        self.config['reddit']['timeframe'] = self.timeframe
        self.config['reddit']['limit'] = self.limit
        self.config['reddit']['subreddit'] = self.subreddit
        self.config['reddit']['section'] = self.section

        # Dislay Config
        self.config['display']['author'] = self.author
        self.config['display']['score'] = self.score

        with open(self.configDir + '/config.json', 'w') as configFile:
            json.dump(self.config, configFile)


    def set(self, flag, value):

        if flag == "subreddit":
            self.subreddit = value
        elif flag == "timeframe":
            self.timeframe = value
        elif flag == "limit":
            self.limit = value
        elif flag == 'section':
            self.section = value

        self.save()

    def get(self, flag=None):
	    if flag == None:
		    return self.config