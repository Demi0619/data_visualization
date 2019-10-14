import requests
import json

url='https://hacker-news.firebaseio.com/v0/item/19155826.json'
r=requests.get(url)
print(r.status_code)
response_dict=r.json()
readable_file='redable_hacker.json'
with open(readable_file,'w') as f1:
    json.dump(response_dict,f1,indent=4)
