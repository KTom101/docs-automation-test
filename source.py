from test import *

data = [] # Array of objects

for item in data:
  # Access the value under the "number" key and print it
  number_value = item["node"]["number"]
  print(generatePrURL(number_value))

  # Access the "edges" array
  edges = item["node"]["files"]["edges"]
  # Loop through each item in the "edges" array
  for edge in edges:
    # Access the "path" key and print its value
    path_value = edge["node"]["path"]
    print(generateDocsURL(path_value))