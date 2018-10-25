
import json

data = {}
data["test"] = "hi"
data["list"] = [1, 2, 3, 4, 5]
for num in data["list"]:
    print(num * 5)
data["people"] = []
data["people"].append({
"name":"Vinul",
"email":"vinul@gmail.com",
"account num": "1234"
})
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)


data = open('data.json')
json_data = json.load(data)
print(json_data)
outfile.close()
