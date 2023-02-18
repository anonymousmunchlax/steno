import json
import itertools

# Load the JSON data from the file
with open("sample3.json") as f:
    data = json.load(f)

# Extract the values from the dictionary
values_only = list(data.values())

# Generate word pairs
word_pairs = list(itertools.combinations(values_only, 2))

# Convert to JSON string
json_str = json.dumps(word_pairs)

# Print the JSON string
print(json_str)