import json
import itertools
from tabulate import tabulate
from docx import Document

# Load the JSON data from the file
with open("sample3.json") as f:
    data = json.load(f)

# Extract the values from the dictionary
values_only = list(data.values())

# Generate word pairs
word_pairs = list(itertools.combinations(values_only, 2))

# Convert to JSON string
json_str = json.dumps(word_pairs)

# Convert JSON string to list
word_pairs_list = json.loads(json_str)

# Generate table data
table_data = [('"{}": "{}",'.format(pair[0], pair[1]),) for pair in word_pairs_list]

# Generate the table string
table_string = tabulate(table_data, tablefmt="plain")

# Create a new document
#document = Document()

# Add the table string as a paragraph to the document
#document.add_paragraph(table_string)

# Save the document
# document.save("output2.docx")

# Print the JSON string
print(table_string)

