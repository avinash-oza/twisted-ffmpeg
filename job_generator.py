import os
import sys
import time
from ftplib import FTP,error_perm,error_temp
from celery_task import encode_video
import argparse
from utils import get_config_option

parser = argparse.ArgumentParser(description='Job Generator')
parser.add_argument('--abs-dir', type=str,help='Specify the absolute path to the DVR directory.')
parser.add_argument('--rel-dir', type=str,help='(NOT USED CURRENTLY)Specify the relative path to the DVR directory.')
parser.add_argument('--date', type=str,help='The date we should process for only in YYYYMMDD format.')
args = parser.parse_args()
check_date_value=None
if args.date is not None:
    check_date_value = args.date

ftp = FTP(host=get_config_option("FTP Settings" , "host"), user=get_config_option("FTP Settings", "username") , passwd=get_config_option("FTP Settings" , "password"))

if args.abs_dir is not None:
    root = args.abs_dir
    num_jobs = 1
    #TODO: Actually implement the date feature
    for root, dirs, files in os.walk(root):
        if len(files):
            file_list = []
            ftp.cwd("/" + get_config_option("FTP Settings" , "root_dir")) 
            try:
                formatted_dir = os.path.splitdrive(root)[1]
                formatted_dir = formatted_dir.replace("\\", "/")
                formatted_dir = formatted_dir[1:] #We need to cut off the leading slash
                ftp.cwd(formatted_dir)
                file_list = ftp.nlst()
            except error_perm:
                # The directory may not even exist if this is a new day
                pass
            for f in files:
               if f.endswith('.avi'):
                    the_file = os.path.join(root, f)
                    the_path = os.path.splitdrive((the_file))
                    final_path = the_path[1].replace("\\", "/")
                    if num_jobs % 10 == 0:
                        print "Sleeping for 10 minutes"
                        time.sleep(600)
                    if f not in file_list:
                        print("{0} -> Adding {1} to list" .format(num_jobs, final_path))
                        encode_video.delay(final_path, "OUTPUT_" + f)
                        num_jobs += 1 #Dont increment unless we actually added a job
                    else:
                        print("{0} ALREADY EXISTS REMOTELY. REMOVING LOCALLY." .format(final_path))
                        os.remove(os.path.join(root, f))
    ftp.quit()
else:
    parser.print_help()
