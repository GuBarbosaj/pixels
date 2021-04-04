#Required libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt

#Variables
pixels_green = 0
pixels_white = 0
pixels_black = 0
pixels = 0

#Reading the file using opencv
data = cv2.imread('Syngenta.bmp')

#Loop that counts the number of pixels of each color
#pixel_green = BGR(0,192,92)
#pixel_white = BGR(255,255,255)
#pixel_black = BGR(0,0,0)
#pixel = all pixels different from the above
for l in data:
    for i in l:
        if i[0] == 0 and i[1] == 192 and i[2] == 96:
            pixels_green += 1
        elif i[0] == 255 and i[1] == 255 and i[2] == 255:
            pixels_white += 1
        elif i[0] == 0 and i[1] == 0 and i[2] == 0:
            pixels_black += 1
        else:
            pixels += 1

#Print counting the number of pixels in the image
print("Pixels Verdes: {}".format(pixels_green))
print("Pixels Brancos: {}".format(pixels_white))
print("Pixels Pretos: {}".format(pixels_black))
print("Pixels: {}".format(pixels))


#Removing white text from the image
for l in data:
    for i in l:
        if i[0] == 255 and i[1] == 255 and i[2] == 255:
           i[0] = 0
           i[1] = 0
           i[2] = 0

#Morphological Transformations
kernel = np.ones((3,3),np.uint8)
dilation = cv2.dilate(data,kernel,iterations = 7)
erosion = cv2.erode(dilation,kernel,iterations = 3)
opening = cv2.morphologyEx(data, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(data, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(erosion, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(data, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(data, cv2.MORPH_BLACKHAT, kernel)

imagens = [data, erosion]
titles = ['Original', 'Modificada']

#Showing the results of morphological operations
for i in range (2):
    plt.subplot(1, 2, i+1), plt.imshow(imagens[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()


