import pprint as pp
import requests as rq

def populatePayload(set, variants):
    total_payloads = []
    payload_list = []

    for collector_num in range( set["Card Count"] ):
        c_num_str = str(collector_num + 1)
        id_entry = {
                "set": set["Set Code"],
        }

        if c_num_str in variants.keys():
            for v in variants[c_num_str]:
                id_entry["collector_number"] = c_num_str + v
                payload_list.append(id_entry.copy())

        else:
            id_entry["collector_number"] = c_num_str
            payload_list.append(id_entry.copy())

        total_payloads = splitReference(payload_list)
    return total_payloads

def processCard(call, payload):
    Card = {}
    Cards = []
    for p in payload:
        response = rq.post(call, json=p).json()
        for c_obj in response['data']:
            Card["Name"]             = c_obj['name']
            Card["Collector Number"] = c_obj['collector_number']
            Card["Colors"]           = c_obj['colors']
            Card["Image Status"]     = c_obj['image_status']
            Card["Image URI"]        = c_obj['image_uris']['small']
            Card["Price"]            = c_obj['prices']['usd']
            Card["Rarity"]           = c_obj['rarity']
            Cards.append(Card.copy())

    return Cards
    
def splitReference(complete_lst):
    reference_limit = 75
    total_lst = []
    partition = len(complete_lst) // reference_limit
    
    for section in range(partition):
        total_lst.append( { 'identifiers' : complete_lst[section * reference_limit : (section + 1) * reference_limit].copy()} )
    total_lst.append( { 'identifiers' : complete_lst[partition * reference_limit : len(complete_lst)].copy() } )

    return total_lst