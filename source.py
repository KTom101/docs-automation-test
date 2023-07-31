from test import *

data = []

for item in data:
  number_value = item["node"]["number"]
  print(generatePrURL(number_value))
  edges = item["node"]["files"]["edges"]
  for edge in edges:
    path_value = edge["node"]["path"]
    print(generateDocsURL(path_value))