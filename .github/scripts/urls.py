# Retrieve Doc Entry URL
def generateDocsURL(file_path):
  path_parts = file_path.split("/")
  url = ""

  if "content" not in path_parts[0]:
    url = "https://github.com/Codecademy/docs/blob/main/"
  else:
    url = "https://www.codecademy.com/resources/docs/"
    for part in path_parts:
      if part == "concepts" or part == "content" or part == "terms" or part.endswith(".md"):
        path_parts.remove(part)

  path_parts = "/".join(path_parts)
  return url + path_parts

# Retrieve PR URL
def generatePrURL(number):
  url = "https://github.com/Codecademy/docs/pull/"
  return url + str(number)

file_path = ""
pr_number = 42

docs_url = generateDocsURL(file_path)
pr_url = generatePrURL(pr_number)

print("Docs URL:", docs_url)
print("PR URL:", pr_url)