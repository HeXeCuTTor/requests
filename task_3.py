
import requests
from pprint import pprint
import time

url = 'https://api.stackexchange.com/2.3/questions?fromdate=1665360000&todate=1665532800&order=desc&sort=activity&site=stackoverflow'
source = requests.get(url)
source_getted = source.json()
for key, value in source_getted.items():
    if key == 'items':
        for dictionaries in value:
            for tag in dictionaries['tags']:
                if tag == 'python':
                    dictionaries['last_activity_date'] = time.ctime(int(dictionaries['last_activity_date']))
                    dictionaries['creation_date'] = time.ctime(int(dictionaries['creation_date']))
                    if 'last_edit_date' in dictionaries.keys():
                        dictionaries['last_edit_date'] = time.ctime(int(dictionaries['last_edit_date']))
                    pprint(dictionaries)
