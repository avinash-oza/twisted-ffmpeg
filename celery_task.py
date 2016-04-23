from subprocess import check_call
from ftplib import FTP,error_perm
from urlparse import urljoin
from celery import Celery
import os
import sys
import urllib
import re
import logging
import random
import time

logging.basicConfig(format= '%(asctime)s ' + "Encoder " +  '%(message)s', level=logging.DEBUG)
#app = Celery('tasks', broker=get_config_option('General', 'broker_url'))
#TODO: Fix this
app = Celery('tasks', broker='1111')

@app.task
def celery_encoder(file_description, file_encoder, file_get_adapter, file_push_adapter=None):
    """This should be the entry point for encoding"""
    #TODO: See if this works
    encoder = CeleryEncoder(file_encoder, file_get_adapter, file_push_adapter)
    encoder.encode_video(file_description)

class CeleryEncoder(object):
    def __init__(self, file_encoder, file_get_adapter, file_push_adapter=None):
        """
        file_encoder: An instance of a FileEncoder object. This will be used to encode the file
        file_get_adapter: An instance of an object from file_transfer_adapters. This will be used to get the file
        file_push_adapter: An instance of an object from file_transfer_adapters. This will the place to upload the file
        """
        self.file_encoder = file_encoder
        self.file_get_adapter = file_get_adapter
        self.file_push_adapter = file_push_adapter if file_push_adapter else self.file_get_adapter

    def encode_video(self, file_description):
        """
        Given a FileDescription object, we get the file, encode it and then upload it to the destination
        """
        # Retrieve our file and keep track of it
        #TODO: This needs to modify the source path to set it to the download directory
        logging.info("Start getting file {0} to local directory".format(file_description.file_name, "LOCAL DIRECTORY"))
        self.file_get_adapter.get_file(file_description)

        #TODO: This needs to be verified
        try:
            self.file_encoder.encode_file(file_description)
        except Exception as e:
            logging.error("Hit exception encoding {0} : {1}".format(file_description.file_name, e))

        else:
            logging.info("Start upload of {0}".format(file_description.file_name))
            self.file_push_adapter.put_file(file_description)
            logging.info("Finished upload of {0}".format(file_description.file_name))
            self.file_get_adapter.clean_up(file_description)

#       server_url = get_config_option("Download Settings", "server_url")
#       root_dir = get_config_option("FTP Settings" , "root_dir")
#       file_path, input_file_name = os.path.split(input_file_path)
#       url = urljoin(server_url, input_file_path.lstrip("\\"))

#       logging.info("Downloading {0}".format(url))
#       try:
#           urllib.urlretrieve(url, input_file_name)
#           logging.info("Finished downloading {0}".format(url))
#       except IOError:
#           delay = random.randrange(40) 
#           logging.info("Seems like server is overloaded. Retrying in {0} seconds.".format(delay))
#           time.sleep(delay)
#           urllib.urlretrieve(url, input_file_name)
#           logging.info("Finished downloading {0}".format(url))

#       ffmpeg_args = ["ffmpeg", "-y", "-i", input_file_name, "-an","-c:v", "libx264", "-b:v", "1024k", output_file_name]
#       
#       if sys.platform.startswith('linux'):
#           logging.info("Linux detected. Modifying command")
#           ffmpeg_args[0] = 'avconv'
#           ffmpeg_args = " ".join(ffmpeg_args)
#       
#       if not check_call(ffmpeg_args, shell=True):
#           ftp = FTP(host=get_config_option("FTP Settings" , "host"), user=get_config_option("FTP Settings", "username") , passwd=get_config_option("FTP Settings" , "password"))
#           ftp.cwd(root_dir)
#           full_path = re.split("/", file_path)
#           for d in full_path:
#               try:
#                   ftp.cwd(d)
#               except error_perm:
#                   ftp.mkd(d)                
#                   ftp.cwd(d)
#           f = open(output_file_name, 'rb')
#           logging.info("Starting upload of {0} as {1}".format(output_file_name, input_file_name))
#           ftp.storbinary('STOR ' + input_file_name, f)
#           logging.info("Finished upload of {0} as {1}".format(output_file_name, input_file_name))
#           ftp.quit()
#           f.close()
            #Remove files after encoding them
#           try:
#               os.remove(input_file_name)
#           except OSError:
#               logging.info("Failed to remove {0}".format(input_file_name))
#               else:
#               logging.info("Removed {0}".format(input_file_name))

#           try:
#               os.remove(output_file_name)
#           except OSError:
#               logging.info("Failed to remove {0}".format(output_file_name))
#           else:
#           logging.info("Removed {0}".format(output_file_name))
if __name__ == "__main__":
    pass
