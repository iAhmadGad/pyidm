import sys
from urllib.request import urlretrieve
import fileinfo
import size_calculator

args = sys.argv
if args[1] == "download":
   url = args[2]
   filename = ""

   if len(args) == 3:
      filename = fileinfo.getName(url)
   else:
      filename = args[3]
      
   path, headers = urlretrieve(url, filename)

   print(filename, "(", size_calculator.calculateSize(int(headers["Content-Length"])), ")", " succesfuly downloaded!")

elif args[1] == "size":
   print(size_calculator.calculateSize(int(fileinfo.getSize(args[2]))))

else:
   print("invalid command\nvalid commands:\npind download <url> <filename>\npind download <url>\npind size <url>")
