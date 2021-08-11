import json


def traverse_recursive(data):
    if("tests" not in data):
        if("details" in data):
            return data["details"]
        elif("name" in data): 
            return data["name"]
        else:
            return "No name or details available."
    else:
        # print("Recursive call********************************************************************************")
        # print(data["tests"])
        print(traverse_recursive(data["tests"]))
    


# Opening JSON file
f = open('results.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
# for i in data['tests']:
#     print(i)
traverse_recursive(data)
  
# Closing file
f.close()
