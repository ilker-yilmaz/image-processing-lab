import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('images/1.jpg', cv2.IMREAD_COLOR)
# img_grayscale = cv2.imread('images/lena.png', cv2.IMREAD_GRAYSCALE)
#plt.imshow(img)



# lena görüntüsünün çözünürlüğünü veren kod

x=0
y=0
for i in img:
    x=x+1
    y=y+1

print(x,y)


