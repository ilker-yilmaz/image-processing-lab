# giriş matrisi al - renkli görüntü
# rgb 3 kanallıdan 8 bitlik  ...
# 3 tane filtre tanımla, filtre matrisin olacak. herhangi bir bilgi kaybı olmadan giriş matrisi üzerinde üzerinde gezdir
# öznitelik matrisi elde et
import cv2

# maksimum ya da ortalama havuza göre girdiye göre çıktı elde et

# havuzlama yöntemiyle elde edilen çıktıyı tek boyutlu diziye çevir

# konvolüsyon matrisi oluştur

# renkli görüntünün alınması

img = cv2.imread('images/1.jpg', cv2.IMREAD_COLOR)
