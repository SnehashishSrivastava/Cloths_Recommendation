import os 
import cv2
import numpy as np
import pandas as pd
from keras.models import Model
from keras.applications import (vgg16)
from sklearn.metrics.pairwise import cosine_similarity

#Model Loading

model = vgg16.VGG16(weights='imagenet')

#Image resizing details

image_width = eval(str(model.layers[0].output.shape[1]))
image_height = eval(str(model.layers[0].output.shape[2]))

#Network Layer selection for vectorization of Images

feature = Model(inputs=model.input,outputs=model.layers[-2].output)

#Input Loading

name=os.listdir('bottoms_resized_png')

a=input("Enter the path of Image")

#name.insert(a,0)

#Data Loading 

images=[]
sample_img = cv2.imread(a)
sample_img=np.resize(sample_img,[image_height,image_width,3])
sample_img=np.expand_dims(sample_img,axis=0)
images.append(sample_img)
for i in name:
    sample_img = cv2.imread("bottoms_resized_png/{}".format(i))
    sample_img=np.resize(sample_img,[image_height,image_width,3])
    sample_img=np.expand_dims(sample_img,axis=0)
    images.append(sample_img)
imag = np.vstack(images)


#Vectorization 0f images

vectors=feature.predict(imag)

#similarity Calculation


similarity = cosine_similarity(vectors)

#tracking back to the image names from 
df=pd.DataFrame(similarity)

#Selectig the top 10 similarities

j=df[0].sort_values(ascending=False)[:11].index

#printing output
for i in j[0:]:
    if(i!=a[20:]):
        print("Suggestions Are: bottoms_resized_png/{}".format(name[i]))
    
