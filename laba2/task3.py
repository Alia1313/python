from PIL import Image, ImageDraw
with Image.open('test.jpg') as img:
    draw = ImageDraw.Draw(img)
    draw.text((113,123),'HELLO')
    img2=Image.open('water.jpg').resize((121,113))
    img.paste(img2,(121,331))
    img.show()
