import json

diagram = {
    "class": "go.GraphLinksModel",
    "nodeDataArray": [
        {"key": 10, "text": "Python Node", "color": "pink"},
        {"key": 20, "text": "Generated", "color": "lightyellow"},
    ],
    "linkDataArray": [
        {"from": 10, "to": 20}
    ]
}

with open("static/data/diagram.json", "w") as f:
    json.dump(diagram, f, indent=2)