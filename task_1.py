
import requests
from pprint import pprint

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
source = requests.get(url)
hero_list = source.json()
intelligence = {}

def find_hero(hero, name):
    if hero['name'] == name:
        for key, values in hero['powerstats'].items():
            if key == 'intelligence':
                intelligence[values] = name

for hero in hero_list:
    name = "Hulk"
    find_hero(hero,name)
    name = "Captain America"
    find_hero(hero,name)
    name = "Thanos"
    find_hero(hero,name)       
print(f'Самый умный супергерой - {sorted(intelligence.values())[-1]}')
