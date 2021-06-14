import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import csv
import pandas
from tensorflow.keras.utils import Sequence

def conv(x):
    if x=='??':
        return -1
    else:
        return int(x,16)


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
    img=Image.fromarray(img,'L')
    img=img.resize((16,256),resample=Image.BOX)
    img=np.array(img)
    img=img.reshape(img.shape[0],img.shape[1],1)
    f.close()
    return img

class ImageSequence(Sequence):
    def __init__(self, x_set, y_set,dir, batch_size):
        self.x, self.y = x_set, y_set
        self.batch_size = batch_size
        self.dir=dir

    def __len__(self):
        return math.ceil(len(self.x) / self.batch_size)

    def __getitem__(self, idx):
        batch_x = self.x[idx * self.batch_size:(idx + 1) *
        self.batch_size]
        batch_y = self.y[idx * self.batch_size:(idx + 1) *
        self.batch_size]

        return np.array([getImage(dir+filename+".bytes") for filename in batch_x]),batch_y
#with open("data/data1.csv",mode='r') as file:
#    csvFile=csv.reader(file)
data=pandas.read_csv("data/data1.csv",header=Image.NONE)
names=data.iloc[:,0].to_numpy()
classes=data.iloc[:,1].to_numpy()
#dir="c:\\Users\\hikma\\Downloads\\"
dir="data\\train\\"

r=ImageSequence(names,classes,dir,10)
#img=getImage(dir+names[0]+".bytes")
#img=getImage(dir+"iTUoxhFD1X6S9lrM8GHq.bytes")
#plt.imshow(img,aspect=8,cmap='gray_r')
#plt.show()
#img.show)


