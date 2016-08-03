'''
Created on Jul 5, 2016

@author: ubuntu
'''

import re
import requests


class Artifact(object):
    '''
    classdocs
    '''

    refs = []

    def __init__(self, uri, internal=False):
        '''
        Constructor
        '''
        self.uri = uri
        self.internal = internal
        self.relationships = []  # list of artifact instances
        Artifact.refs.append(self)

    def relate(self, other):
        self.relationships.append(other)
        other.relationships.append(self)

    def score(self, scorer):
        top = scorer(self.uri, self.internal)
        self.relationships = top

    def get_features(self):
        # needs lots of expansion, assuming text for now
        response = requests.get(self.uri)
        feats = re.findall(r'\w+|[^\s\w]', response.content.decode())

        return feats

    @classmethod
    def train(cls):
        for ref in cls.refs[:1000]:
            print('training', ref)

if __name__ == '__main__':
    import string
    from random import choice
    letters = list(string.ascii_letters)

    for i in range(1000000):
        url = ''.join(choice(letters) for i in range(50))
        a = Artifact(url)

    Artifact.train()
