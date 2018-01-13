class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}
    def increment_ngram(self, word):
        if word == '':
            self.count ++
    def get_count(self, ngram):
