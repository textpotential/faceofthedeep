"""
A module that has the capacity to automate the search process. For example,
the `search_google` function below will search Google for images like this:

>>> search_results = search('Genesis 1:2')
>>> search_results
[{'displayLink': 'www.knowing-jesus.com',
 'htmlSnippet': '<b>Genesis 1-2</b> The Earth Was ...',
 'htmlTitle': '<b>Genesis 1:2</b> Verse of the Day',
 'image': {'byteSize': 55259,
           'contextLink': 'http://www.knowing-jesus.com/genesis-1-3-2/',
           'height': 405,
           'thumbnailHeight': 99,
           'thumbnailLink': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQLvewTSE2LijZTJJ283e-u3HVvBYG9ric_DaiBW7GAf36DNhTV2QVDYRRz',
           'thumbnailWidth': 132,
           'width': 540},
 'kind': 'customsearch#result',
 'link': 'http://cdn.knowing-jesus.com/wp-content/uploads/Genesis-1-2-The-Earth-Was-WIthour-Form-And-Void-blue-copy.jpg',
 'mime': 'image/jpeg',
 'snippet': 'Genesis 1-2 The Earth Was ...',
 'title': 'Genesis 1:2 Verse of the Day'},
...]

(Note the 'link' key in the first search result above.)

NOTE WELL: THE FREE VERSION OF THE GOOGLE CUSTOM SEARCH LIMITS
THE NUMBER OF QUERIES TO 100 PER DAY!!!
"""

from googleapiclient.discovery import build


# To obtain the following credentials, follow the instructions here:
# http://stackoverflow.com/a/37084643/1775603
API_KEY = "<*****>"  # Put your api key here.
CSE_ID = "<*****>"  # Put your custom search id here.


def search_google(search_term):
    service = build("customsearch", "v1", developerKey=API_KEY)
    result = service.cse().list(q=search_term, cx=CSE_ID,
                                searchType="image").execute()
    return result['items']


if __name__ == '__main__':
    from pprint import pprint
    search_results = search_google('Genesis 1:2')
    for result in search_results:
        pprint(result)
