import filename

def getExtension(url):
  splittedPath = filename.getName(url).split(".")
  return splittedPath[len(splittedPath) - 1]
