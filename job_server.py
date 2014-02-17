from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web.static import File
from twisted.internet import reactor

import cgi
import logging
logging.basicConfig(format= '%(asctime)s' + " Server: " +  '%(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

class JobProvider (Resource):
    def __init__(self):
        Resource.__init__(self)

    def render_GET(self, request):
        logging.info("Job Provider Called")
        return "This is the job provider" + '<html><body><form method="POST"><input name="the-field" type="text" /></form></body></html>'

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
