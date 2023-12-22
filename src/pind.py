import sys
from urllib.request import urlretrieve
import fileinfo
import size_calculator

args = sys.argv
if args[1] == "download" and (len(args) == 3 or len(args) == 4):
   url = args[2]
   filename = ""

   if len(args) == 3:
      filename = fileinfo.getName(url)
   else:
      filename = args[3]
      
   path, headers = urlretrieve(url, filename)

   print(filename, "(", size_calculator.calculateSize(int(headers["Content-Length"])), ")", " succesfuly downloaded!")

elif args[1] == "size" and len(args) == 3:
   print(fileinfo.getSize(args[2]))

else:
   print("invalid arguments\nvalid syntax:\npind download <url> <filename>\npind download <url>\npind size <url>")
