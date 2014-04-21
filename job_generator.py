import os
import sys
import time
from celery_task import encode_video

root = sys.argv[1]
num_jobs = 0
#TODO: Accept a date at the command line to only add those jobs
for root, dirs, files in os.walk(root):
    if len(files):
        for f in files:
           if f.endswith('.avi'):
                the_file = os.path.join(root, f)
                the_path = os.path.splitdrive((the_file))
                final_path = the_path[1].replace("\\", "/")
                num_jobs += 1
                if num_jobs % 10 == 0:
                    print "Sleeping for 5 minutes"
                    time.sleep(300)
                print("Adding {0} to list" .format(final_path))
                encode_video.delay(final_path, "OUTPUT_" + f)
