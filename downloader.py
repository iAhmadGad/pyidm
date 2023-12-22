from urllib.request import urlretrieve

def download(url, pathname):
   path, headers =  urlretrieve(url, pathname)
   print(filename, "(", filesize.calculateSize(int(headers["Content-Length"])), ")", "succesfuly downloaded!")
