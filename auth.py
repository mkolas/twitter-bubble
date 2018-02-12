import base64

import requests

bearer_token = 'your-bearer-token-here'
encoded_token = base64.b64encode(bearer_token.encode()).decode("utf-8")
print(str(encoded_token))
headers = dict()
headers['Authorization'] = "Basic " + str(encoded_token)
headers['Content-Type'] = "application/x-www-form-urlencoded;charset=UTF-8"


r = requests.post(url="https://api.twitter.com/oauth2/token", data="grant_type=client_credentials", headers=headers)
access_token = r.json()['access_token']
print(access_token)
headers['Authorization'] = "Bearer " + access_token
r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json",
                 params=dict(q="*", count=100, result_type='recent', lang='en', tweet_mode='extended'),
                 headers=headers)
print(r.json())
print(len(r.json()['statuses']))
filtered = [x['full_text'] for x in r.json()['statuses'] if '🌹' in x['user']['name']]
print(len(filtered))
print(filtered)
