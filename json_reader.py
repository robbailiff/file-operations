import json
with open("C:\Python Projects\Scrapy_project\stack\items.json", "r") as read_file:
    data = json.load(read_file)
    print(json.dumps(data, indent=4))