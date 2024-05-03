
import time
import subprocess
import os
import threading

from ftplib import FTP
from hashlib import new
import json
from urllib import response
import urllib.request
import zipfile
import os
import shutil



class auto_start():
    def __init__(self):
        pass
    def run_roscore(self):
    	# print("roscore")
        cmd = "gnome-terminal -e 'bash -c \"rosclean purge -y && roscore\"'"
        os.system(cmd)
        
        print("1.roscore")
    
  
    def clean_ros(self):
        cmd = f"gnome-terminal -e \"bash -c 'python3 -V && python3 -V && python3 -V && rosclean purge -y'\""
        subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
        # subprocess.Popen("rosclean purge -y",stdout=subprocess.PIPE, shell=True)
        

    def imu(self):
        print("roscore")
        cmd = "gnome-terminal -e 'bash -c \"rosrun  handsfree_ros_imu hfi_a9_ros.py\"'"
        os.system(cmd)



    
    def ekf(self):
    	# print("roscore")
        cmd = "gnome-terminal -e 'bash -c \"rosrun  handsfree_ros_imu hfi_a9_ros.py\"'"
        os.system(cmd)
        

 

    

    def run(self):
        print('4.Run')
        path = "/home/nguyenhoang/System/lanchqr.py"
        os.system(f"gnome-terminal -e 'bash -c \"python3 {path}\"'")


if __name__ == "__main__":

    


    a = auto_start()
    t1 = threading.Thread(target=a.run_roscore)
    t5 = threading.Thread(target= a.imu)
    t4 = threading.Thread(target= a.run)


    t1.start()
    time.sleep(1)

  
    
    t5.start()
    time.sleep(1)
    
 

    t4.start()
    time.sleep(1)





