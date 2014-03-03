import Queue
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web.static import File
from twisted.internet import reactor

import cgi
import yaml
import logging
logging.basicConfig(format= '%(asctime)s' + " Server: " +  '%(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

class JobProvider (Resource):
    def __init__(self):
        Resource.__init__(self)
        self.available_jobs = Queue.Queue()
        
        log.info("Loading pending jobs from file")
        jobs = self.get_pending_jobs()
        for job in jobs:
            self.available_jobs.put(job)
        log.info("Finished adding " + str(len(jobs)) + " pending video files")
    def get_pending_jobs(self):
        """
        Gives a new file name for the client to download and convert
        """
        jobs = set()
        f = open("data.yaml", 'r')
        jobs = yaml.load(f.read())
        return jobs

    def render_GET(self, request):
        try:
            file_path = self.available_jobs.get(block=False)
            log.info("TBD HOST:" + "Provided file " + file_path + "as encoding task") 
            
            return yaml.dump([file_path])
#           return "This is the job provider" + '<html><body><form method="POST"><input name="the-field" type="text" /></form></body></html>'
        except Queue.Empty,e:
            file_path = None
            log.info("TBD_HOST:" +" NO FILES AVAILABLE TO ENCODE") 
            return yaml.dump([])
    def render_POST(self, request):
        logging.info("Got " + str(request.args['the-field']))
        return '<html><body>You submitted: %s</body></html>' % (cgi.escape(request.args["the-field"][0]),)
class Calender(Resource):
    def getChild(self, name, request):
        return YearPage(int(name))

if __name__ == '__main__':
    resource = Resource()
    resource.putChild("job_handler", JobProvider())

    factory = Site(resource)
    reactor.listenTCP(8888,factory)
    reactor.run()
