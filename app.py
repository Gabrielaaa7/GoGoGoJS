import json

nodes = [
    {"key": 1, "name": "Miton C", "type": "company"},
    {"key": 2, "name": "Munchained SE", "type": "company"},
    {"key": 3, "name": "Martin Hála", "type": "person"},
    {"key": 4, "name": "Note about Miton C", "type": "note", "relatedTo": 1}
]

links = [
    {"from": 1, "to": 2},
    {"from": 1, "to": 3},
    {"from": 4, "to": 1, "category": "noteLink"}
]

data = {
    "nodes": nodes,
    "links": links
}

with open("static/data/graph.json", "w") as f:
    json.dump(data, f, indent=2)