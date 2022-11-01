from PIL import Image

# read image
img = Image.open("images/lena.png")

def rotate_picture_90_left(img: Image) -> Image:
    w, h = img.size
    pixels = img.load()
    img_new = Image.new('RGB', (h, w))
    pixels_new = img_new.load()
    for y in range(h):
        for x in range(w):
            pixels_new[y, w-x-1] = pixels[x, y]

    # save image to desktop
    img_new.save('C:/Users/ilker/Desktop/rotated_image.png')
    return img_new


rotate_picture_90_left(img)
rotate_picture_90_left(img)
