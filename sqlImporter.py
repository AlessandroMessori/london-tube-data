import json

tube_data_file = open('./train-network.json')

tube_data = json.load(tube_data_file)

print(tube_data)