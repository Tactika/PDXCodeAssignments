from PIL import Image
import colorsys

img = Image.open("lenna.png")  # must be in same folder
width, height = img.size
pixels = img.load()


for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # your code here
        r = r - 170  # int(0.114*r + 0.587*g + 0.299*b)
        g = g + 2  # int(0.499*r + 0.787*g + 0.314*b)
        b = b - 20  # int(0.199*r + 0.487*g + 0.014*b)

        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[i, j] = (r, g, b)

img.show()
