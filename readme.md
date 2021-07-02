# Data
The .bytes file were extracted from the data. There are 10868 of them.
Those were divided into 6 parts, each 2000 files except the last one 868
The names of those parts are bytes_names.1,.2,.3,.4,.5,.6
The actual files are in 7z format bytes.1.7z,....

## CSV files

the names of the files were combined with the corresonding classes extracted from the trainLabels.csv to
obtain the data.1.csv,....

## Resized images

The images were resized using the resized-data.py and stored as follows

the 9000 images from 1,2,3,5 and the second half of 4 are stored as training data
the 1868 images from 6 and the first part of 4 were stored as test data. Both train and test
were compressed into the resized.7z file

# Code

1. keras_cifar10.ipynb example of image classification using CNN
1. keras_cifar10-generator.ipynb the same as the above but the images are loaded on the fly
1. malware-resized-yuan.ipynb malware classification of resized images which are assume to be on local disk
1. malware-yuan-kaggle.ipynb same as the above but the resized.7z is download from the google drive
1. malware-yuan.ipynb resizes images on the fly 
1. malware.ipynb old attempt
