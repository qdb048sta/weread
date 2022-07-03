import os
size=0
os.chdir("E:\\照片\\")
#os.mkdir("D:\\愛美桌布\\")
import shutil
import os.path, time
from datetime import datetime
import pandas as pd
removed_list=[]
counter=0
for i in os.listdir("E:\\照片\\"):
    if ".jpg" in i or ".jfif" in i and counter<=100:
        size=size+os.stat(i).st_size
        
        filetime=os.path.getmtime("E:\\照片\\"+i)
        current=datetime(2020,1,1).timestamp()
        #print(current)
        counter=counter+1
        if filetime<current:
            os.remove("E:\\照片\\"+i)
            removed_list.append(i)

pd.DataFrame(removed_list).to_csv("C:\\Users\\starg\\removed_file2.csv")
print(size/(1024*1024*1024))