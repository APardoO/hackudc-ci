import json

# Step 1: Load the JSON Data from the file 'codee-checks1.json'
file_path_new = './codee-checks.json'

# Open and read the JSON file to load the data
with open(file_path_new, 'r') as file:
    json_data_new = json.load(file)

# Display a brief overview of the loaded JSON data structure
json_data_new.keys(), type(json_data_new["Checks"]), len(json_data_new["Checks"])

# Step 2: Create the SARIF Report Skeleton
sarif_skeleton = {
    "$schema": "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0-rtm.5.json",
    "version": "2.1.0",
    "runs": [{
        "tool": {
            "driver": {
                "name": "Custom Code Analysis Tool",  # Placeholder name, to be replaced with actual tool name if available
                "version": "1.0",  # Placeholder version, to be replaced with actual version if available
                "rules": []  # This will be populated with analysis rules derived from the checks
            }
        },
        "results": [],  # This will be populated with the results of the checks
    }]
}

# Display the SARIF report skeleton
#print(sarif_skeleton)

# Step 3: Map JSON Checks to SARIF Results
for check in json_data_new["Checks"]:
    # Parse the file path and line number from Location
    location_parts = check["Location"].split(':')
    file_path = location_parts[0]
    start_line = int(location_parts[1])

    # Construct the SARIF result for this check
    result = {
        "ruleId": check["Check"],
        "level": "warning" if check["Level"] == "L1" else "note",  # Assuming 'L1' maps to 'warning', others to 'note'
        "message": {
            "text": f"{check['Title']}. Suggestion: {check['Suggestion']}"
        },
        "locations": [{
            "physicalLocation": {
                "artifactLocation": {
                    "uri": file_path
                },
                "region": {
                    "startLine": start_line
                }
            }
        }]
    }
    
    # Append this result to the SARIF results list
    sarif_skeleton["runs"][0]["results"].append(result)

    # Check if the rule for this check is already added, if not, add it
    rule_ids = [rule["id"] for rule in sarif_skeleton["runs"][0]["tool"]["driver"]["rules"]]
    if check["Check"] not in rule_ids:
        sarif_skeleton["runs"][0]["tool"]["driver"]["rules"].append({
            "id": check["Check"],
            "name": check["Title"],
            "shortDescription": {
                "text": check["Title"]
            },
            "fullDescription": {
                "text": check["Suggestion"]
            },
            "help": {
                "text": check["Suggestion"],
                "markdown": check["Suggestion"]
            }
        })

# Displayo the count of results and rules added to the SARIF report to verify the mapping
len(sarif_skeleton["runs"][0]["results"]), len(sarif_skeleton["runs"][0]["tool"]["driver"]["rules"])

# Step 4: Populate Tool and Run Information
# Update the tool name and version based on the JSON 'Analysis' section, if available
sarif_skeleton["runs"][0]["tool"]["driver"]["name"] = "Codee Analysis Tool"  # Example name
sarif_skeleton["runs"][0]["tool"]["driver"]["version"] = "2024.1.1"  # Example version from provided data

# Assuming the 'CompilerFlags' could represent the command line options used, we include it in the invocations
sarif_skeleton["runs"][0]["invocations"] = [{
    "commandLine": json_data_new["Analysis"].get("CompilerFlags", ""),
    "executionSuccessful": True  # Assuming the analysis was successful
}]

# Since the detailed tool information (e.g., informationUri) was not provided, we keep the placeholders or make reasonable assumptions

# Verify the updated tool and run information
sarif_skeleton["runs"][0]["tool"]["driver"]["name"], sarif_skeleton["runs"][0]["tool"]["driver"]["version"], sarif_skeleton["runs"][0]["invocations"]

# Save the filtered checks to the specified file

# Specify the file path and name
file_path = 'priority.sharif'

# Open the file in write mode and write the contents of `text` to it
with open(file_path, 'w') as file:
    json.dump(sarif_skeleton, file, indent=4)
