from twisted.internet import reactor,defer
from twisted.web.client import Agent,getPage
from twisted.web.http_headers import Headers
import urllib
import logging

logging.basicConfig(format= '%(asctime)s' + " Client: " +  '%(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

def getNewJobs():
    d = defer.Deferred()
    reactor.callLater(2, d.callback, None)
    getPage("http://127.0.0.1:8888/job_handler", method='POST', postdata=urllib.urlencode({'the-field':'Script_test'}),
    headers = {'Content-Type':'application/x-www-form-urlencoded'})
    return d

def printLog(d):
    log.info("Got the callback")

def cbStop(d):
    reactor.stop()

d = getNewJobs()
d.addCallback(printLog)
d.addCallback(cbStop)

reactor.run()
