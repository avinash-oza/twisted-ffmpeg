from twisted.internet import protocol

#FFMPEG COMMAND. TO BE MOVED TO CONFIG
ffmpeg_args = ["avconv", "-i", "file1.avi", "-preset", "faster", "-crf", "21", "output.avi"]


class WCProcessProtocol(protocol.ProcessProtocol):

    def __init__(self):
        self.data = ""
    def connectionMade(self):
        self.transport.write("")
        self.transport.closeStdin()
    
    def outConnectionLost(self):
        print "Reached connection lost"
        self.transport.loseConnection()
        self.receiveCounts()

    def receiveCounts(self):
        print "Recieve counts"
     
    def processExited(self, status):
        print status

    def errReceived(self,data):
        print "Err"
        print data

from twisted.internet import reactor
wcProcess = WCProcessProtocol()
ffmpeg_args[7] = "test2.avi"
reactor.spawnProcess(wcProcess, 'avconv', args=ffmpeg_args)
reactor.run()
