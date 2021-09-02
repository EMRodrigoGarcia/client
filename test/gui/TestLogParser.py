import json
import sys

# Method that tries to find the data using nested loops
def traverse_loop(data):
    failing_tests = []

    # Loop level 0 where we loop through all the feature files inside the only test suites that we have.
    for feature_file in data["tests"][0]["tests"]:

        # Loop through all the features in the feature file
        for feature in feature_file['tests']:

            # Loop through all the scenarios in the feature
            for scenario in feature['tests']:

                # If the scenario is not skipped, then loop through all the steps in the scenario
                if "tests" not in scenario:
                    break
                for test_step in scenario['tests']:

                    # If the test step fails then it contains further "tests" object
                    # So loop through all the errors in the test step
                    if "tests" not in test_step:
                        break
                    for error in test_step['tests']:

                        # Append the information of failing tests into the list of failing tests
                        test = {
                            "Feature File": str(feature_file['name']),
                            "Feature": str(feature['name']),
                            "Scenario": str(scenario['name']),
                            "Test Step": str(test_step['name']),
                            "Error Details": str(error['detail']),
                        }

                        failing_tests.append(test)

    # return unique node in the failing_tests
    return map(dict, set(tuple(sorted(d.items())) for d in failing_tests))


# Opening JSON file
f = open(str(sys.argv[1]))

# returns JSON object as
# a dictionary
data = json.load(f)

# Traverse through the json file to look for failing tests
failing_tests = traverse_loop(data)
# print(failing_tests)
print(json.dumps(failing_tests, indent=4, sort_keys=True))

# Closing file
f.close()
