import xmlrpclib

server = xmlrpclib.Server('http://192.168.2.50:8000')
print server.printmsg("This is a test")

