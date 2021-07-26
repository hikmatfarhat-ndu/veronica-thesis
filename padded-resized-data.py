import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import csv
import pandas
import os

def conv(x):
    if x=='??':
        return -1
    else:
        return int(x,16)

mclass=9
df=pandas.read_csv("data/trainLabels.csv",header=None,names=['id','mclass'])
newdf=df[df.mclass==mclass]
print(len(newdf.index))
names=newdf.iloc[:,0].to_numpy()
# classes=data.iloc[:,1].to_numpy()
dict={1:"Ramnit",2:"Lollipop",3:"Kelihos_ver3",4:"Vundo",5:"Simda",6:"Tracur",7:"Kelihos_ver1",8:"Obfuscator",9:"Gatak"}
dir="c:/Users/hikma/source/repos/veronica-thesis/data/train/"
resized_dir="c:/Users/hikma/source/repos/veronica-thesis/data/padded-resized/train/"
#for k in dict.keys():
#   os.mkdir(resized_dir+dict[k])
def getSize(filename):
    f=open(filename)
    rest=f.read()
    lines=rest.splitlines()
    f.close()
    return len(lines)
def getImage(filename,max):
    f=open(filename)
    rest=f.read()
    lines=rest.splitlines()
    f.close()
    img=[]
    for line in lines:
        el=line.split()
        el=list(map(conv,el))
        if(len(el)==17):
            img.append(el[1:])
    img=np.asarray(img,dtype=np.uint8)
    print("original shape ={}".format(img.shape))
    r=img.shape[0]
    d=max-r
    z=np.zeros((d,16))
    img=np.vstack((img,z))
    print("new shape ={}".format(img.shape))

    img=Image.fromarray(img,'L')
    img=img.resize((256,256),resample=Image.LANCZOS)
    return img
# for name,c in zip(names,classes):
max=0
for name in names:
   s=getSize(dir+name+".bytes")
   if(s>max):
       max=s

 
for name in names:
    img=getImage(dir+name+".bytes",max)
    img.save(resized_dir+dict[mclass]+"/"+name+".png")

