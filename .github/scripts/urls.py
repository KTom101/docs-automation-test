# Retrieve Doc Entry URL
def generateDocsURL(file_path):
  url = "https://www.codecademy.com/resources/docs/"
  path_parts = file_path.split("/")
  # Add case for files in documentation folder
  for part in path_parts:
    if part == "concepts" or part == "content" or part == "terms" or part.endswith(".md"):
      path_parts.remove(part)
  # end cases
  path_parts = "/".join(path_parts)
  print (url + path_parts)

# Retrieve PR URL
def generatePrURL(number):
  url = "https://github.com/Codecademy/docs/pull/"
  print (url + str(number))
