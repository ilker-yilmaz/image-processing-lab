from turtledemo.planet_and_moon import G

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('images/lena.png')

print(img.shape)

# Show image
print(img)

# lena görüntüsünü ekrana basan kod
#plt.imshow(img)

# görüntüyü gez ve birinci ve üçüncü sütunları değiştir
for i in img:
    for j in i:
        j[0],j[2] = j[2],j[0]

# görüntüyü ekrana bas
print("değişimden sonra:")
print(img)

cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(G,cmap="gray")
