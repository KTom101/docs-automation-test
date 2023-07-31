def generateDocsURL(file_path):
  url = "https://www.codecademy.com/resources/docs/"
  path_parts = file_path.split("/")
  # Add cases for files that are in the documentation folder
  for part in path_parts:
    if part == "concepts" or part == "content" or part == "terms" or part.endswith(".md"):
      path_parts.remove(part)
  # end cases
  path_parts = "/".join(path_parts)
  print (url + path_parts)

def generatePrURL(number):
  url = "https://github.com/Codecademy/docs/pull/"
  print (url + str(number))
