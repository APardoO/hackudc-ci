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
        try:
            # Split the command into parts for subprocess.run
            # This is important for safely executing the command without shell=True
            command_parts = command.split()
            
            # Execute the command
            result = subprocess.run(command_parts, check=True, text=True, capture_output=True)
            
            # Print the stdout and stderr of the command
            print(f"Command executed successfully: {command}\nOutput: {result.stdout}")
            if result.stderr:
                print(f"Errors: {result.stderr}")
        except subprocess.CalledProcessError as e:
            # Handle errors in the executed command
            print(f"Error executing command: {command}\nError: {e}")
# Example usage
if __name__ == "__main__":
    json_file_path = 'filtered_sorted_checks_with_autofix.json'
    json_data = load_json_file(json_file_path)
    commands = extract_commands(json_data)
    execute_commands(commands)

