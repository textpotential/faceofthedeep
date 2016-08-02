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

    def __init__(self, uri, internal=False):
        '''
        Constructor
        '''
        self.uri = uri
        self.internal = internal
        self.relationships = [] # list of artifact instances
        print('I am made :).')
    
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