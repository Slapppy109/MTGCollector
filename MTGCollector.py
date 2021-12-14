import pprint as pp
import requests as rq
import MTGCollector_helper as MTGh

collection_call = "https://api.scryfall.com/cards/collection"

Unglued = {
    "Name"       : "Unglued",
    "Set Code"   : "ugl",
    "Card Count" : 88,
    "Cards"      : []
}

Unhinged = {
    "Name"       : "Unhinged",
    "Set Code"   : "unh",
    "Card Count" : 141,
    "Cards"      : []
}

Unstable = {
    "Name"       : "Unstable",
    "Set Code"   : "ust",
    "Card Count" : 216,
    "Cards"      : []
}

Unstable_variants = {
    '3'  : ['a', 'b', 'c', 'd'],
    '12' : ['a', 'b', 'c', 'd', 'e', 'f'],
    '41' : ['a', 'b', 'c', 'd'],
    '49' : ['a', 'b', 'c', 'd', 'e', 'f'],
    '54' : ['a', 'b', 'c', 'd'],
    '67' : ['a', 'b', 'c', 'd', 'e', 'f'],
    '82' : ['a', 'b', 'c', 'd', 'e', 'f'],
    '98' : ['a', 'b', 'c', 'd'],
    '103' : ['a', 'b', 'c', 'd'],
    '113' : ['a', 'b', 'c', 'd', 'e', 'f'],
    '145' : ['a', 'b', 'c', 'd'],
    '147' : ['a', 'b', 'c', 'd', 'e', 'f'],
    '165' : ['a', 'b', 'c', 'd', 'e'],
}

No_variants = {}

ungluedPayload  = MTGh.populatePayload(Unglued, No_variants)
unhingedPayload = MTGh.populatePayload(Unhinged, No_variants)
unstablePayload = MTGh.populatePayload(Unstable, Unstable_variants)

# pp.pprint(ungluedPayload)
# pp.pprint(unhingedPayload)
# pp.pprint(unstablePayload)
Unglued["Cards"]  = MTGh.processCard(collection_call, ungluedPayload)
Unhinged["Cards"] = MTGh.processCard(collection_call, unhingedPayload)
Unstable["Cards"] = MTGh.processCard(collection_call, unstablePayload)

# print(len(Unglued["Cards"]))
# print(len(Unhinged["Cards"]))
# print(len(Unstable["Cards"]))
