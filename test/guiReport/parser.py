import json

# Method that tries to find the data using nested loops
def traverse_loop(data):
    failing_tests = []
    
    for feature_file in  data["tests"][0]["tests"]:
        # Loop level 0 where we loop inside the tets suite
        # print(str(feature_file['name']), " has len ", str(len(feature_file['tests'])))
        for feature in feature_file['tests']:
            # print(str(feature['name']), " has len ", str(len(feature['tests'])))
            for scenario in feature['tests']:
                if("tests" not in scenario): break
                # print(str(scenario['name']), " has len ", str(len(scenario['tests'])))
                for test_step in scenario['tests']:
                    if("tests" not in test_step): break
                    for error in test_step['tests']:
                        test = {"Feature_file": str(feature_file['name']),
                        "Feature": str(feature['name']),
                        "Scenario": str(scenario['name']),
                        "Test Step": str(test_step['name']),
                        "Error Details": str(error['detail'])
                        }
                        failing_tests.append(test)

    return failing_tests



# Opening JSON file
f = open('test.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Traverse through the json file to look for failing tests
failing_tests = traverse_loop(data)
print(failing_tests)


# Closing file
f.close()