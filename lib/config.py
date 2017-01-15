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

        self.timeframe = self.config['config']['timeframe']
        self.limit = self.config['config']['limit']
        self.subreddit = self.config['config']['subreddit']
        self.section = self.config['config']['section']


    def save(self):
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