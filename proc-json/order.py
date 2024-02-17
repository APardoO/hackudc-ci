import json

# Function to load JSON content from a file
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Load both JSON files
codee_screening = load_json('./codee-screening.json')
codee_checks1 = load_json('./codee-checks1.json')

# Extract the "Ranking of Checkers" and flatten the list of lists
ranking_of_checkers = [checker for sublist in codee_screening['Ranking of Checkers'] for checker in sublist]

# Create a mapping of checker names to their priorities
priority_map = {checker_detail['Checker']: int(checker_detail['Priority'][1:]) for checker_detail in ranking_of_checkers}

# Extract the checks
checks = codee_checks1['Checks']

# Sort the checks based on the priority of their checkers
sorted_checks = sorted(checks, key=lambda x: priority_map.get(x['Check'], float('inf')))

# Filter the sorted checks to include only those with a non-empty 'Auto-fix' field
sorted_checks_with_autofix = [check for check in sorted_checks if check.get('Auto-fix')]

# Define the path for the new JSON file to save checks with non-empty 'Auto-fix'
filtered_checks_file_path = './filtered_sorted_checks_with_autofix.json'

# Save the filtered checks to the specified file
with open(filtered_checks_file_path, 'w') as file:
    json.dump(sorted_checks_with_autofix, file, indent=4)
