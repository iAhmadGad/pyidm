import sys, fileinfo, downloader, configurator

SYNTAX ="pyidm syntax:\npyidm download <url> <filename>\npyidm download <url>\npyidm info <url> <requested-info>\npydim config <key> <value>"

args = sys.argv

if args[1] == "download" and (len(args) == 3 or len(args) == 4):
   if len(args) == 3:
      downloader.download(args[2], fileinfo.getInfo(args[2], 'n'))
   else:
      downloader.download(args[2], args[3])

elif args[1] == "info" and len(args) == 4:
   for i in range(len(args[3])):
      print(fileinfo.getInfo(args[2], args[3][i]))
      
elif args[1] == "config" and len(args) == 4:
   configure(args[2], args[3])
   
elif args[1] == "help" and len(args) == 2:
   print(SYNTAX)
   
else:
   print("invalid arguments", SYNTAX)
