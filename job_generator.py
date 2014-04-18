import os
import sys

root = sys.argv[1]
for root, dirs, files in os.walk(root):
    if len(files):
        for file in files:
           if file.endswith('.avi'):
                print("Adding {0} to list" .format(os.path.join(root,file)))
