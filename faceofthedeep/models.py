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


def appmaker(zodb_root):
    if 'app_root' not in zodb_root:
        app_root = Face()
        first_artifact = PassageArtifacts('Genesis 1:1')
        first_artifact.relate('בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃')
        first_artifact.relate('In the beginning when God created '
                              'the heavens and the earth, . . .')
        first_artifact.relate('https://upload.wikimedia.org/wikipedia/'
                              'commons/1/1a/William_de_Brailes_-'
                              '_First_Two_Days_of_Creation_%28'
                              'Genesis_1_-_1-8%29_-_Walters_W1061R_-'
                              '_Full_Page.jpg')
        first_artifact.relate('https://upload.wikimedia.org/wikipedia/'
                              'commons/3/3e/Ifc_mall_Void_201108.jpg')
        first_artifact.relate('https://upload.wikimedia.org/wikipedia/'
                              'commons/b/b3/Genesis_on_egg_cropped.jpg')
        first_artifact.relate('https://upload.wikimedia.org/wikipedia/'
                              'commons/f/f3/Genesis_Chapter_One_'
                              'from_a_1620-21_King_James_Bible.jpg')
        app_root[first_artifact.ref] = first_artifact
        first_artifact.__name__ = first_artifact.ref
        first_artifact.__parent__ = app_root
        zodb_root['app_root'] = app_root
        import transaction
        transaction.commit()
    return zodb_root['app_root']
