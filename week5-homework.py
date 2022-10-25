# maksimum havuzlama yöntemi uygulanmış bir örnek
import cv2
import numpy as np
from matplotlib import pyplot as plt

# giriş matrisi, filtre matrisi, çıktı matrisi

# giriş matrisi
# img = cv2.imread('images/lena.png', cv2.IMREAD_COLOR)
#
# # filtre matrisi
# filter = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
#
# # çıktı matrisi
# output = np.zeros((img.shape[0] - 2, img.shape[1] - 2, 3), dtype=np.uint8)
#
# # maksimum havuzlama yöntemi
# for i in range(img.shape[0] - 2):
#     for j in range(img.shape[1] - 2):
#         for k in range(3):
#             output[i, j, k] = np.max(img[i:i + 3, j:j + 3, k])
#
# # çıktı matrisinin gösterilmesi
# plt.imshow(output)
# plt.show()
#
# # input, convolution, output
#
# # input
# img = cv2.imread('images/lena.png', cv2.IMREAD_COLOR)
#
# # convolution
# filter = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
#
# # output
# output = np.zeros((img.shape[0] - 2, img.shape[1] - 2, 3), dtype=np.uint8)
#
# # convolution
# for i in range(img.shape[0] - 2):
#     for j in range(img.shape[1] - 2):
#         for k in range(3):
#             output[i, j, k] = np.max(img[i:i + 3, j:j + 3, k])
#
# # output
# plt.imshow(output)
# plt.show()

# input, convolution, feature maps, pooling, (feature extraction), output

# input
img = cv2.imread('images/lena.png', cv2.IMREAD_COLOR)

# convolution
filter = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

# feature maps
feature_maps = np.zeros((img.shape[0] - 2, img.shape[1] - 2, 3), dtype=np.uint8)

# pooling
output = np.zeros((img.shape[0] - 2, img.shape[1] - 2, 3), dtype=np.uint8)

# convolution
for i in range(img.shape[0] - 2):
    for j in range(img.shape[1] - 2):
        for k in range(3):
            feature_maps[i, j, k] = np.max(img[i:i + 3, j:j + 3, k])

# pooling
for i in range(img.shape[0] - 2):
    for j in range(img.shape[1] - 2):
        for k in range(3):
            output[i, j, k] = np.max(feature_maps[i:i + 3, j:j + 3, k])

# output
plt.imshow(output)
plt.show()

# print size of output
print(img.shape)
print(output.shape)

# print file size of output
print(img.nbytes)
print(output.nbytes)