from PIL import Image

base_img=Image.open("image2.jpg")
image_filter=Image.open("filter1.jpg")

size=(760,760)

base_img=base_img.resize(size)
image_filter=image_filter.resize(size)

r,g,b=base_img.split()
R,G,B=image_filter.split()

im=Image.merge("RGB",(g,R,b))
im.show()
# im.save('1_merged.jpg')

