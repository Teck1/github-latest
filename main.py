import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    print(username)

    response = requests.get("https://api.github.com/users/{}/events".format(username))

    events = json.loads(response.content)

    print("Event total count: {}".format(len(events)))
    print("Latest event: {}".format(events[0]['created_at']))
    print("Event type: {}".format(events[0]['type']))


