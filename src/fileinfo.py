from urllib.request import urlopen
import filename, filesize, fileextension

def getFullInfo(url):
    return urlopen(url).info().getheaders()

def getInfo(url, request):
    if request == 'n':
        return filename.getName(url)
    elif request == 's':
        return filesize.getSize(url)
    elif request == 'e':
        return fileextension.getExtension(url)
