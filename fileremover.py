import time
import os
import shutil

file1 = "file1.txt"
days = 35
ctime = os.stat(file1).st_ctime
currenttime = time.time()
day30 = 30*24*60*60

if currenttime - ctime > day30 :
    os.remove(file1)

else :
    print("the file is less than 30days old")    

print(ctime)
print(time.time())