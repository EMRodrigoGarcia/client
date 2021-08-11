import json

# Method that tries to find the data using nested loops
def traverse_loop(data):
    # logSize = len(data["tests"][0]["tests"])
    # print(logSize)
    
    for i in  data["tests"][0]["tests"]:
        # Loop level 0 where we loop inside the tets suite
        print(str(i['name']), " has len ", str(len(i['tests'])))

    # print(data["tests"][0]["tests"][1]["tests"][0]["tests"][0]["tests"][5]["tests"][0])




# Method that tries to find the data recursively
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
        # item = next(iter(filter(lambda x: x['name'] == name, items)), None)
        print(traverse_recursive(data["tests"]))
    


# Opening JSON file
f = open('test.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
# for i in data['tests']:
    # print(i)
# traverse_recursive(data)
traverse_loop(data)


# Closing file
f.close()
