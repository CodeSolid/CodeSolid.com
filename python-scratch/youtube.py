import json
import csv
import pprint as pp
import csv

def process_csv(items):
    keys = items[0].keys()
    with open('python-scratch/playlist.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(items)
    pass

def process_items(item_list: list):
    items = []
    for i in item_list:
        new_item = {}
        snippet = i["snippet"]
        new_item["playlistId"] = snippet["playlistId"]
        new_item["videoId"] = snippet["resourceId"]["videoId"]
        new_item["title"] = snippet["title"]
        new_item["description"] = snippet["description"]
        new_item["position"] = snippet["position"]
        items.append(new_item)
    return items 

with open('python-scratch/Professor_leonard_calc_2_playlistItems.json') as f:
	data = json.load(f)
	items = process_items(data.get("items"))
	process_csv(items)
	pp.pprint(items)