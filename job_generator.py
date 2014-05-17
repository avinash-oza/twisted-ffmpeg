import os
import sys
import time
from ftplib import FTP,error_perm,error_temp
from celery_task import encode_video
import argparse
from utils import get_config_option


def get_ftp_connection():
    ftp = FTP(host=get_config_option("FTP Settings" , "host"), user=get_config_option("FTP Settings", "username") , passwd=get_config_option("FTP Settings" , "password"))
    
    return ftp

def generate_jobs(abs_dir):

    ftp = get_ftp_connection()
    if abs_dir is not None:
        root = abs_dir
        num_jobs = 1
        #TODO: Actually implement the date feature
        for root, dirs, files in os.walk(root):
            if len(files):
                file_list = []
                try:
                    ftp.cwd("/" + get_config_option("FTP Settings" , "root_dir")) 
                    formatted_dir = os.path.splitdrive(root)[1]
                    formatted_dir = formatted_dir.replace("\\", "/")
                    formatted_dir = formatted_dir[1:] #We need to cut off the leading slash
                    ftp.cwd(formatted_dir)
                    file_list = ftp.nlst()
                except error_perm:
                    # Occurs if there is no directory of the name we are looking for
                    print (formatted_dir + "NOT FOUND")
                    pass
                except error_temp:
                    print "Seems like FTP connection was lost. Reconnecting"
                    ftp = get_ftp_connection()
                for f in files:
                   if f.endswith('.avi'):
                        the_file = os.path.join(root, f)
                        the_path = os.path.splitdrive((the_file))
                        final_path = the_path[1].replace("\\", "/")
                        if not clean_old and num_jobs % 10 == 0:
                            print "Sleeping for 10 minutes"
                            time.sleep(600)
                        if f not in file_list:
                            if not clean_old:
                                print("{0} -> Adding {1} to list" .format(num_jobs, final_path))
                                encode_video.delay(final_path, "OUTPUT_" + f)
                                num_jobs += 1 #Dont increment unless we actually added a job
                        else:
                            print("{0} ALREADY EXISTS REMOTELY. REMOVING LOCALLY." .format(final_path))
                            os.remove(os.path.join(root, f))
        ftp.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Job Generator')
    parser.add_argument('abs_dir', type=str,help='Specify the absolute path to the directory to encode.')
    parser.add_argument('--date', type=str,help='The date we should process for only in YYYYMMDD format.')
    parser.add_argument('--clean-old', action='store_true',help='Clean up files that have already been encoded.')
    args = parser.parse_args()
    check_date_value=None
    clean_old = False

    if args.clean_old:
        clean_old = True
#       import ipdb; ipdb.set_trace()
    if args.date is not None:
        check_date_value = args.date
    if args.abs_dir is not None:
        generate_jobs(args.abs_dir)
    else:
        parser.print_help()
        
