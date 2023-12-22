from urllib.request import urlretrieve
from filesize_calculator import getSize

url = input("url: ")
filename = input("filename: ")

path, headers = urlretrieve(url, filename)
print("size:", getSize(int(headers["Content-Length"])))
    
