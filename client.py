from twisted.internet import reactor,defer
from twisted.web.client import Agent,getPage
from twisted.web.http_headers import Headers
import urllib
import logging
import yaml
import random
import time

logging.basicConfig(format= '%(asctime)s' + " Client: " +  '%(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

class Client(object):
    def getNewJobs(self):
    #   d = defer.Deferred()
        self.d = getPage("http://127.0.0.1:8888/job_handler")
        reactor.callLater(2, self.processJob, None)
        return self.d

    def sleep(self, secs):
        d = defer.Deferred()
        reactor.callLater(secs, d.callback, None)
        return d

    def processJob(self, result):
        d = self.d
        self.d = None
        if result is None:
            #TODO : Add logic here to retry after a random interval
    #       retry = random.randint(30, 60)
            retry = 10
            log.info("No jobs available. Trying again in " + str(retry) + " seconds." )
            time.sleep(retry)
            log.info("Slept")
            self.d = self.getNewJobs()
        else:
            # Got a job, time to process it
            file_name = yaml.load(result)[0]
            log.info("Got file " + file_name)

client = Client()        
d = client.getNewJobs()
d.addCallback(client.processJob)

#   getPage("http://127.0.0.1:8888/job_handler", method='POST', postdata=urllib.urlencode({'the-field':'Script_test'}),
#   headers = {'Content-Type':'application/x-www-form-urlencoded'})
reactor.run()
