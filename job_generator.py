import os
import sys
from celery_task import encode_video

root = sys.argv[1]
for root, dirs, files in os.walk(root):
    if len(files):
        for f in files:
           if f.endswith('.avi'):
                the_file = os.path.join(root, f)
                the_path = os.path.splitdrive((the_file))
                final_path = the_path[1].replace("\\", "/")
                print("Adding {0} to list" .format(final_path))
                encode_video(final_path, "OUTPUT_" + f)
