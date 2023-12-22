from urllib.request import urlretrieve
import filesize

def download(url, filepath):
    path, headers = urlretrieve(url, filepath)

    print(filepath, "(", filesize.calculateSize(int(headers["Content-Length"])), ")", " succesfuly downloaded!")
