"""
This is a simple standalone http server that supports getting a file and deleting a file. There is no authentication or any protection so use wisely!
"""
import os
import sys
import logging
import yaml
from bottle import Bottle, run, request, static_file
from application_config import ApplicationConfig
logging.basicConfig(format= '%(asctime)s ' + '%(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

app = Bottle()

@app.route('/get_file_list')
def get_file_list():
    config = ApplicationConfig('bottle_http_server.cfg')
    file_root = config.get_config_option('Default', 'root_directory')
    log.info("file_root is {0}".format(file_root))

    final_file_paths = []
    for dir_path, _, filenames in os.walk(file_root):
        for filename in filenames:
            #TODO: Make this configurable
            if filename.endswith('.avi'):
                # Strip out the base path so that it looks more like a relative path that can be used
                base_path = dir_path.replace(file_root + os.sep, "")
                final_file_paths.append(os.path.join(base_path, filename))

    final_results = {'number_of_entries' : len(final_file_paths),
                     'file_paths' : final_file_paths
                    }
    return yaml.dump(final_results)

@app.route('/get_file/<file_to_get:path>')
def get_file(file_to_get):
    config = ApplicationConfig('bottle_http_server.cfg')
    file_root = config.get_config_option('Default', 'root_directory')

    full_file_path = os.path.join(file_root, file_to_get)
    log.info("Full file root {0}".format(full_file_path))
    directory, file_name = os.path.split(full_file_path)
    log.info("File to get is {0}    {1}".format(directory, file_name))

    return static_file(file_name, root=directory)




run(app, host='localhost', port=8080)
