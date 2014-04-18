from subprocess import check_call
from ftplib import FTP,error_perm
from celery import Celery
import os
import urllib
import re
import logging
from utils import get_config_option

logging.basicConfig(format= '%(asctime)s ' + "Encoder " +  '%(message)s', level=logging.DEBUG)
app = Celery('tasks', broker=get_config_option('General', 'broker_url'))

@app.task
def encode_video(input_file_path, output_file_name):
    """
    We first obtain the video via http, encode it, and then upload it back
    """
    server_url = get_config_option("Download Settings", "server_url")
    root_dir = get_config_option("FTP Settings" , "root_dir")
    file_path, input_file_name = os.path.split(input_file_path)
    logging.info("Downloading file {0} from {1}".format(input_file_path, server_url))
    urllib.urlretrieve(server_url + input_file_path, input_file_name)
    logging.info("Finished downloading {0}".format(input_file_path))

    ffmpeg_args = ["ffmpeg", "-y", "-i", input_file_name, "-an", "-b:v", "1024k", output_file_name]
    if not check_call(ffmpeg_args, shell=True):
        ftp = FTP(host=get_config_option("FTP Settings" , "host"), user=get_config_option("FTP Settings", "username") , passwd=get_config_option("FTP Settings" , "password"))
        ftp.cwd(root_dir)
        full_path = re.split("/", file_path)
        for d in full_path:
            try:
                ftp.cwd(d)
            except error_perm:
                ftp.mkd(d)                
                ftp.cwd(d)
        f = open(output_file_name, 'rb')
        logging.info("Starting upload of {0} as {1}".format(output_file_name, input_file_name))
        ftp.storbinary('STOR ' + input_file_name, f)
        logging.info("Finished upload of {0} as {1}".format(output_file_name, input_file_name))
        ftp.quit()
        f.close()
        #Remove files after encoding them
        try:
            os.remove(input_file_name)
        except OSError:
            logging.info("Failed to remove {0}".format(input_file_name))
        else:
            logging.info("Removed {0}".format(input_file_name))

        try:
            os.remove(output_file_name)
        except OSError:
            logging.info("Failed to remove {0}".format(output_file_name))
        else:
            logging.info("Removed {0}".format(output_file_name))
if __name__ == "__main__":
    pass
