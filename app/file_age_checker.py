import time
import os
from glob import glob

# the time to delete the pictures
time_to_delete = time.time() - 1

# 10080 for 7 days
# 1440 for 1 day
# 60 for 1 minute

# paths to directories
my_list = os.listdir('static/images')
file_path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(file_path, "static/images") 

# Deletes the file after a certain time
os.chdir(image_path)
for image in my_list:
    if image.endswith("jpg") or image.endswith("jpeg") or image.endswith("png"):
        st=os.stat(image)
        mtime=st.st_mtime
        print(st)
        if mtime < time_to_delete:
            print('remove %s'%image)
            os.unlink(image) # uncomment only if you are sure
