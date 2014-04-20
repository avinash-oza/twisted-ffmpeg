import os
import sys
from celery_task import encode_video

root = sys.argv[1]
for root, dirs, files in os.walk(root):
    if len(files):
        for f in files:
           if f.endswith('.avi'):
                the_file = os.path.join(root, f)
                print("Adding {0} to list" .format(the_file))
                encode_video(the_file, f + "-out")
