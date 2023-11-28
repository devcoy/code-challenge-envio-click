import json

file_path = 'input_02.json'

with open(file_path, 'r') as input_file:
    data_array = json.load(input_file)

input_file.close()
print("Array from file:", data_array)