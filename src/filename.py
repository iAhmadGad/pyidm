from urllib.parse import urlparse

def getName(url):
  splittedPath = urlparse(url).path.split("/")
  return splittedPath[len(splittedPath) - 1]
