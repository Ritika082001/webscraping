import os
import json
import time
import random
file=open("task5.json","r+")
a=json.load(file)
file.close()
def text():
    for i in a:
        path="/home/admin123/Desktop/projects/task9/task9"+i["movie_name"]+".json"
        if os.path.exists(path):
            pass
        else:
            data=open(path,"w+")
            json.dump(i,data,indent=4)  
text()