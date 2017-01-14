#!/usr/local/bin/python3

from reddit import Reddit
from thought import Thought

connection = Reddit()

# connection.pull("all", "250")

connection.read()
print(connection.randomThought())