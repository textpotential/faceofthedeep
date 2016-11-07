from random import random
import re

from persistent import Persistent
from persistent.mapping import PersistentMapping


class Face(PersistentMapping):
    __parent__ = None
    __name__ = None


class PassageArtifacts(Persistent):

    """
    Creates a collection of artifacts for a specific passage.
    (Can contain other PassageArtifacts instances as an artifact.)
    """

    def __init__(self, ref):
        """
        Constructor
        """
        self.ref = ref
        self.__name__ = ref
        self.relations = set()

    @property
    def text_type_data(self, num=50):
        text_types = []
        for other in self.score()[:num]:
            if isinstance(other, PassageArtifacts):
                # eventually need to look through top
                # of other self.relations
                text_types.append((other.ref, 'text'))
            # assuming the rest are strings (but may need adj.)
            elif other.startswith(('/', 'http')):
                # assuming an image
                text_types.append((other, 'image'))
            else:
                text_types.append((other, 'text'))
        return text_types

    def relate(self, other):
        self.relations.add(other)
        if isinstance(other, PassageArtifacts):
            other.relations.add(self)

    def score(self, scorer=random):
        """
        Score every relation between 0 and 1, with 1
        being the strongest relation--a working-strategy.
        """
        return sorted(self.relations, key=lambda x: scorer())

