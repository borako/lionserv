import SimpleXMLRPCServer

class TestFunctions:
    def printmsg(msg, astr):
        print (msg)	
        return ("msg printed")


server = SimpleXMLRPCServer.SimpleXMLRPCServer(("192.168.2.50", 8000))
server.register_instance(TestFunctions())
server.serve_forever()
