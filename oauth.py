GITHUB_API = 'https://api.github.com'


import requests
import getpass
import json
from urlparse import urljoin


def main():
    #
    # User Input
    #
    username = raw_input('Github username: ')
    password = getpass.getpass('Github password: ')
    note = raw_input('Note: ')
    #
    # Compose Request
    #
    url = urljoin(GITHUB_API, 'authorizations')
    payload = {}
    if note:
        payload['note'] = note
    res = requests.post(
        url,
        auth = (username, password),
        data = json.dumps(payload),
        )
    #
    # Parse Response
    #
    j = json.loads(res.text)
    if res.status_code >= 400:
        msg = j.get('message', 'UNDEFINED ERROR (no error description from server)')
        print 'ERROR: %s' % msg
        return
    token = j['token']
    print 'New token: %s' % token

    with open("tokenfile", "w") as token_file:
        token_file.write(token)
    
if __name__ == '__main__':
    main()
