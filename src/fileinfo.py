from urllib.request import urlopen
from urllib.parse import urlparse
from size_calculator import calculateSize

def getInfo(url):
    return urlopen(url).info().getheaders()

def getName(url):
    splittedPath =  urlparse(url).path.split("/")
    return splittedPath[len(splittedPath) - 1]
                        
def getSize(url):
    return calculateSize(int(urlopen(url).info().getheaders("Content-Length")[0]))
