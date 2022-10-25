import cv2
from matplotlib import pyplot as plt

# ödev:
# elimizde aynı çözünürlükte iki resim var. sadece resimleri farklı. bu iki görüntü birbirine yüzde kaç benziyor.
# iki görüntüyü gezerek pikselleri karşılaştır. ve yüzdeyi bul. aynı olan toplam piksel sayısını toplam çözünürlüğe böl.
# yüzdeyi bul.

# 1. resmi oku
img1 = cv2.imread("images/image1.png", cv2.IMREAD_GRAYSCALE)
# 2. resmi oku
img2 = cv2.imread("images/image2.png", cv2.IMREAD_GRAYSCALE)


# resimlerin çözünürlüklerini 400x400 olarak ayarla
img1 = cv2.resize(img1, (400, 400))
img2 = cv2.resize(img2, (400, 400))


# resimlerin çözünürlüklerini bul
x1 = 0
y1 = 0
for i in img1:
    x1 = x1 + 1
    y1 = y1 + 1

x2 = 0
y2 = 0
for i in img2:
    x2 = x2 + 1
    y2 = y2 + 1


# resimlerin çözünürlüklerini ekrana bas
print("1. resmin çözünürlüğü: ", x1, y1)
print("2. resmin çözünürlüğü: ", x2, y2)

# resimlerin çözünürlüklerini karşılaştır
if x1 != x2 or y1 != y2:
    print("resimlerin çözünürlükleri farklı. işlem yapılamaz.")
    exit()

# resimlerin çözünürlüklerini ekrana bas
print("resimlerin çözünürlükleri aynı. işlem yapılabilir.")

# resimleri gezerek pikselleri karşılaştır
fark = 0
for i in range(x1):
    for j in range(y1):
        if img1[i][j] != img2[i][j]:
            fark = fark + 1

# yüzdeyi bul
yuzde = (fark / (x1 * y1)) * 100

# yüzdeyi ekrana bas
print("resimlerin yüzdesi: ", yuzde)
