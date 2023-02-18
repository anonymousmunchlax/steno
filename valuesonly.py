import json

# Load the JSON data from the file
with open("sample3.json") as f:
    data = json.load(f)

# Extract the keys from the dictionary and convert to JSON string
values_only = list(data.keys())
json_str = json.dumps(values_only)

# Print the JSON string
print(json_str)