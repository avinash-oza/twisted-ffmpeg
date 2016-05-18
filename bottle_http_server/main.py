"""
This is a simple standalone http server that supports getting a file and deleting a file. There is no authentication or any protection so use wisely!
"""
import os
import sys
import logging
import yaml
from bottle import Bottle, run, request
from application_config import ApplicationConfig
logging.basicConfig(format= '%(asctime)s ' + '%(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

app = Bottle()

@app.route('/get_file_list')
def get_file_list():
    config = ApplicationConfig('bottle_http_server.cfg')
    file_root = config.get_config_option('Default', 'root_directory')
    log.info("file_root is {0}".format(file_root))
#   addressing_scheme, network_location, path, query, fragment_identifier = request.urlparts
#   log.info("Request url is {0}".format(network_location))

    final_file_paths = []
    for dir_path, _, filenames in os.walk(file_root):
        for filename in filenames:
            #TODO: Make this configurable
            if filename.endswith('.avi'):
                final_file_paths.append(os.path.join(dir_path, filename))

    final_results = {'number_of_entries' : len(final_file_paths),
                     'file_paths' : final_file_paths
                    }
    return yaml.dump(final_results)



run(app, host='localhost', port=8080)
