import requests as rq
import pprint as pp

url = "https://api.scryfall.com/sets"

test = rq.get(url).json()

target_sets = {"Unglued", "Unhinged", "Unstable", "Unfinity"}
sets = []
for i in test['data']:
    if i['name'] in target_sets:
        sets.append(i)
   
pp.pprint(sets)