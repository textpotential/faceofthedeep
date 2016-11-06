"""
This module adds a single new relation to the existing database of
`PassageArtifacts`. Expand the middle section of this module to automate
the database insertions rather than to add manually. Or add several
manually (and create a function to add), if you'd prefer.
"""

import transaction
import ZODB, ZODB.FileStorage


# Note that this script should be in the same directory as `Data.fs`.
# Open the datbase and get the root.
db = ZODB.DB('Data.fs')
connection = db.open()
root = connection.root

###############################################################################
# Add to database (automate this--use a for clause, for example).
###############################################################################

# Now get the `Genesis 1:1` PassageArtifacts instance that was previously saved.
gen_1_1 = root.app_root['Genesis 1:1']

print(gen_1_1.relations)

# Add a new relation.
gen_1_1.relate('https://lh3.googleusercontent.com/-e2kQFsSbH0Y/AAAAAAAAAAI/'
               'AAAAAAAAAdY/_nuYB6f2VVM/s500-c-no/photo.jpg')
# We have to let ZODB know that the `relations` set has changed.
# Otherwise, ZODB will simply see that it still has the set and
# will not notice any change. Think of `_p_` as short for persistence.
gen_1_1._p_changed = True

# Commit the changes
transaction.commit()

###############################################################################
# Now just print results and clean up. Database has been updated.
###############################################################################

print(gen_1_1.relations)

# Close the database
db.close()

###############################################################################
# The app will now have another image when viewed in the browser.
###############################################################################
