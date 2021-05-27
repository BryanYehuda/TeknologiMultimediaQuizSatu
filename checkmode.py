from PIL import Image
img = Image.open('cmyk.jpg')
mode = img.mode
print(mode)