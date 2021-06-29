import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import csv
import pandas
#from tensorflow.keras.utils import Sequence

def conv(x):
    if x=='??':
        return -1
    else:
        return int(x,16)


# class CIFAR10Sequence(Sequence):
#     def __init__(self, x_set, y_set, batch_size):
#         self.x, self.y = x_set, y_set
#         self.batch_size = batch_size

#     def __len__(self):
#         return math.ceil(len(self.x) / self.batch_size)

#     def __getitem__(self, idx):
#         batch_x = self.x[idx * self.batch_size:(idx + 1) *
#         self.batch_size]
#         batch_y = self.y[idx * self.batch_size:(idx + 1) *
#         self.batch_size]

#         return np.array([plt.imread(filename) for filename in batch_x]),batch_y
#with open("data/data.1.csv",mode='r') as file:
#    csvFile=csv.reader(file)
data=pandas.read_csv("data/data.1.csv",header=None)
names=data.iloc[:,0].to_numpy()
classes=data.iloc[:,1].to_numpy()
dir="c:/Users/hikma/source/repos/veronica-thesis/data/train/"
#f=open(dir+"FVmO980BKzIHYiGUscDx.bytes")
#f=open(dir+"iTUoxhFD1X6S9lrM8GHq.bytes")
#f=open("jyTeVvz3dUCLuwgAtlEO.bytes")
#f=open("ksTyZ4jN21lBiC9UYOGe.bytes")
#f=open("Kvxm20yICftr8djGVqUA.bytes")
#f=open("0ACDbR5M3ZhBJajygTuf.bytes")
#f=open("0A32eTdBKayjCWhZqDOQ.bytes")
#f=open("short")
def getSize(filename):
    f=open(filename)
    rest=f.read()
    lines=rest.splitlines()
    return len(lines)
def getImage(filename):
    f=open(filename)
    rest=f.read()
    lines=rest.splitlines()
    img=[]
    for line in lines:
        el=line.split()
        el=list(map(conv,el))
        if(len(el)==17):
            img.append(el[1:])
    img=np.asarray(img,dtype=np.uint8)
    print("original shape ={}".format(img.shape))
    img=Image.fromarray(img,'L')
    img=img.resize((256,256),resample=Image.LANCZOS)
    return img
#f=open("data/train/"+names[0]+".bytes")
# min=0
# max=0
# c=9
# for i,n in enumerate(names):
#     if classes[i]==c:
#      s=getSize("data/train/"+n+".bytes")
#      if max == 0 or s > max:
#          max=s
#      if min ==0 or s < min:
#          min=s
# print("range of class {} is {}-{}".format(c,min,max))
img=getImage(dir+names[0]+".bytes")
img.save("c:/Users/hikma/source/repos/veronica-thesis/data/resized/"+names[0]+".png")

#img=getImage(dir+"FVmO980BKzIHYiGUscDx.bytes")
#img=np.asarray(img,dtype=np.uint8)
#img=np.transpose(img)
#print(type(img[0,0]))
#print(img[0:10])
#img=Image.fromarray(img,'L')
#img=img.resize((256,16))
#img=img.resize((256,16),resample=Image.LANCZOS)
#img=img.resize((256,16),resample=Image.NEAREST)
#img=img.resize((256,16),resample=Image.HAMMING)
#img=img.resize((256,16),resample=Image.BOX)
#a=np.array(img)
#a=a.reshape(a.shape[0],a.shape[1],1)
#print(a.shape)
#plt.imshow(img,aspect=0.1,cmap='gray_r')
#plt.show()
#img.show)


