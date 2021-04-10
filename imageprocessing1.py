from PIL import Image, ImageFilter
img = Image.open("./images/pikachu.jpg")
filtered = img.filter(ImageFilter.BLUR)
filtered.save('blur.jpeg', "jpeg")
print(img.mode)
