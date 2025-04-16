# !!! This is not work properly !!!!

from scipy.misc import imread, imsave, imresize 
img = imread('Advance Python/myimg.jpg')
print(img.dtype, img.shape)
img_tint = img * [1,0.95,0.9]
img_tint = imresize(img_tint,(300,300))
imsave('Advance Python/myimg_1.jpg',img_tint)
