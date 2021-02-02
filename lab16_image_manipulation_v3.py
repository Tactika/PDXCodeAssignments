from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

# Draw the head
draw.ellipse(((200, 125, 300, 200)), fill=(0, 0, 0) , width = 2)

color = (60, 80, 25) 
# Draw the body
draw.line((250, 150, 250, 350), fill=color)
draw.line((150, 250, 350, 250), fill=color)
draw.line((250, 350, 150, 450), fill=color)
#draw.line((250, 350, 150, 250), fill=color)


img.show()
