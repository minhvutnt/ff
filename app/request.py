import requests
import json

def request_link(link):
    all_leader_request = requests.get(link)
    content = all_leader_request.content.decode("utf8")
    js = json.loads(content)
    return js
