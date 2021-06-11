import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
def conv(x):
    if x=='??':
        return -1
    else:
        return int(x,16)

#f=open("FVmO980BKzIHYiGUscDx.bytes")
f=open("iTUoxhFD1X6S9lrM8GHq.bytes")
#f=open("jyTeVvz3dUCLuwgAtlEO.bytes")
#f=open("ksTyZ4jN21lBiC9UYOGe.bytes")
#f=open("Kvxm20yICftr8djGVqUA.bytes")
#f=open("0ACDbR5M3ZhBJajygTuf.bytes")
#f=open("0A32eTdBKayjCWhZqDOQ.bytes")
#f=open("short")
rest=f.read()
lines=rest.splitlines()
img=[]
for line in lines:
   el=line.split()
   el=list(map(conv,el))
   if(len(el)==17):
     img.append(el[1:])


img=np.asarray(img,dtype=np.uint8)
#img=np.transpose(img)
print(type(img[0,0]))
print(img[0:10])
img=Image.fromarray(img,'L')
#img=img.resize((256,16))
#img=img.resize((256,16),resample=Image.LANCZOS)
#img=img.resize((256,16),resample=Image.NEAREST)
#img=img.resize((256,16),resample=Image.HAMMING)
img=img.resize((256,16),resample=Image.BOX)
plt.imshow(img,aspect=8,cmap='gray_r')
plt.show()
#img.show)
