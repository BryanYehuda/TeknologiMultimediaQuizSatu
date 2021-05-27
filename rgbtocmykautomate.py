from PIL import Image
img = Image.open('RGB.jpg')
cmyk_image = img.convert('CMYK')
cmyk_image.save('cmykautomate.jpg')