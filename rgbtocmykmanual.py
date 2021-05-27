rgb_scale = 255

def rgb_to_cmyk(r,g,b):
    r_ = r/255
    g_ = g/255
    b_ = b/255
    k = 1 - max(r_,g_,b_)
    if (r == 0) and (g == 0) and (b == 0):
        # black
        return 0, 0, 0, k

    # Rumus RGB ke CMYK
    else:
        c = (1-r_-k)/(1-k)
        m = (1-g_-k)/(1-k)
        y = (1-b_-k)/(1-k)

    
    return c*rgb_scale, m*rgb_scale, y*rgb_scale, k*rgb_scale


from PIL import Image, ImageDraw
# Membuka Gambar
im = Image.open('RGB.jpg')
# Membuat wadah baru untuk gambar CMYK
img = Image.new('CMYK', (im.width,im.height))
draw = ImageDraw.Draw(img)

for i in range(im.width):
    for j in range(im.height):
        # Mengakses setiap pixel pada gambar
        rgb = im.getpixel((i, j))
        # Mengubah RGB ke CMYK
        cmyk = (rgb_to_cmyk(rgb[0], rgb[1], rgb[2]))
        draw.point((i,j), fill=(int(cmyk[0]),int(cmyk[1]),int(cmyk[2]),int(cmyk[3])) )
img.save("cmyk.jpg")