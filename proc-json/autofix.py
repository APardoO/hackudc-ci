import json

def load_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)
# This code snippet should be added to autofix.py
# Including safety measures for executing Python code

def extract_commands(json_data):
    second_commands = []
    for item in json_data:
        # Check if 'Auto-fix' exists and has at least two commands
        if 'Auto-fix' in item and len(item['Auto-fix']) >= 2:
            # Extract the second command
            second_command = item['Auto-fix'][1]  # Index 1 for the second command
            second_commands.append(second_command.strip())  # Strip to remove leading/trailing whitespace
    return second_commands

def execute_commands(commands):
    for command in commands:
        print(f"Executing command: {command}")
        # Here you would call the appropriate system or subprocess function to execute the command
        # Remember to validate and sanitize the command string to prevent security issues

# Example usage
if __name__ == "__main__":
    json_file_path = 'filtered_sorted_checks_with_autofix.json'
    json_data = load_json_file(json_file_path)
    commands = extract_commands(json_data)
    execute_commands(commands)

