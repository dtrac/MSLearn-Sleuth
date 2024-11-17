# requests_example.py
import requests, json, os, sys
from datetime import datetime

try:
    response = requests.get("https://api.github.com")
    response.raise_for_status()  # Will raise an HTTPError for bad responses (4xx, 5xx)

    # Parsing JSON into a Python object (dictionary or list)
    data = response.json()
    
    #print(data)  # Print the entire data to inspect it

    # Print the status code
    print(f"Status Code: {response.status_code}")

    # Print the entire JSON object in a pretty-printed format
    print(json.dumps(data, indent=4))  # The `indent=4` makes the output more readable

    print(f"Current user URL: {data['current_user_url']}")  # Access a specific key

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")


# uses OS module
    
# Get current working directory
current_directory = os.getcwd()
print(f"Current directory: {current_directory}")

# List files and directories in the current directory
files = os.listdir('.')
print(f"Files in current directory: {files}")

# Directory path
dir_path = 'new_directory'

# Check if the directory already exists
if not os.path.exists(dir_path):
    os.mkdir(dir_path)
    print(f"Directory '{dir_path}' created.")
else:
    print(f"Directory '{dir_path}' already exists.")




# uses sys module
# Get Python version
print(f"Python version: {sys.version}")

# Get the list of command line arguments passed to the script
print(f"Command line arguments: {sys.argv}")



# datetime
# Get current date and time
now = datetime.now()
print(f"Current date and time: {now}")

# Format the current date in a specific format
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date and time: {formatted_date}")

# Get just the current date
current_date = now.date()
print(f"Today's date: {current_date}")

# Get just the current time
current_time = now.time()
print(f"Current time: {current_time}")


# Exiting the program with a status code
sys.exit(1)