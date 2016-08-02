import requests
#from pprint import pprint

def get_verse(api_token, book, chapt, verse):
    
    endpoint = 'https://bibles.org/v2/versions.js'
    pw_fake = 'X'

    request = requests.get(endpoint, auth=(api_token, pw_fake))
    versions = request.json()

    for version in versions['response']['versions']:
        version_id = version['id']
        #print(version_id)
        passage_endpoint = 'https://bibles.org/v2/passages.js?q[]={book}+{chapt}:{verse}&version={versionid}'
        p_ep = passage_endpoint.format(book=book, chapt=chapt, verse=verse, versionid=version_id)
        #print(p_ep)
        req_pas = requests.get(p_ep, auth=(api_token, pw_fake))
        #print(req_pas.url)
        passage = req_pas.json()
        #pprint(passage)
        response = passage.get('response')
        if response:
            search = response.get('search')
            if search:
                result = search.get('result')
                if result:
                    passages = result.get('passages')
                    if passages:
                        for passage in passages:
                            print(passage['version'], passage['text'])
#     pas_version = passage['response']['search']['result']['passages']['version']
#     pas_text = passage['response']['search']['result']['passages']['text']
#     
#     print(pas_version, ':', pas_text)
#     

#     url = 'https://bibles.org/v2/verses/' + version_id + ':' + verse + '.js'
#     response = requests.get(url, auth=(api_token, pw_fake))
#     verse = response.json()
#     print(verse)
#     