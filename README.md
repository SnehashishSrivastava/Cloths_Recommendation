# FlixStock_assesment
 The experementation and pocs are done in the Assignment_poc.ipynb
 only the Solution.py should be accepted as the final solution 
 The Final solution uses basic cosine similarity technique to finde items with similar vectors.
 The Vectorizarion is done using VGG16 Imagenet weight models
 
 
The Flow of proram is as follows :
1. The Model(VGG16) is loaded and last layer is removed 
2. Database(bottoms_resized_png) is loaded 
3. Input image path is taken
4.All the images in the database and the input image is resized in the size of CNN model used in vgg16
5.Input image is stacked on the total data
6. Vector is calculated
7.Cosine Similarity is calculated
8. Output image path are displayed



Possible Changes that will result in better performance of our model is changing the vectorizing model and replacing it with cloth specific network that defferentiates between different clothing accecories in general the VGG16 default classes has not class like "pants" or "Skirts" or any other modern clothing.
