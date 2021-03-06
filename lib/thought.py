class Thought():

    def __init__(self, data):
        self.text = data['title']
        self.subtext = data['selftext']
        self.author = data['author']
        self.permalink = "https://reddit.com" + data['permalink']
        self.score = data['score']
        self.created = data['created']
        self.nsfw = data['over_18']
        self.id = data['id']

    def __str__(self):
        return self.text + '\n -' + self.author

    def __repr__(self):
        return "Thought: " + self.id

    def jsonExport(self):
        return {
            'title': self.text,
            'author': self.author,
            'permalink': self.permalink,
            'id': self.id
        }
