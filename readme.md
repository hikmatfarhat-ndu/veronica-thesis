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
