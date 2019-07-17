from PIL import Image
#open the images
base_img=Image.open("image2.jpg")
image_filter=Image.open("filter1.jpg")

size=(760,760)
#resize the images to the same size
base_img=base_img.resize(size)
image_filter=image_filter.resize(size)
#split the images in RGB format
r,g,b=base_img.split()
R,G,B=image_filter.split()
#Merge the images
im=Image.merge("RGB",(g,R,b))
im.show()
im.save('1_merged.jpg')

