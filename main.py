from PIL import Image 
import os 

original_img = 'original.jpg'
output_grey = 'img_out_grey.png'
output_resized = 'img_out_resized.png'
output_pdf = 'img_out_pdf.pdf'

#Dimensão máxima da imagem final
output_width = 1024

#Abre imagem original
img_original = Image.open(original_img)

#Converte imagem para tons de cinza
img_grey = img_original.convert('LA')
img_grey.save(output_grey)

#Obtém dimensões da imagem atual
width, height = img_grey.size

#Reduz imagem, se necessário
if width > output_width:
    size_rate = output_width / width
    size = int(width * size_rate), int(height * size_rate)
    im_resized = img_grey.resize(size, Image.ANTIALIAS)
else:
    im_resized = img_grey

im_resized.save(output_resized, "PNG")

#Converte para PDF
im1 = im_resized.convert('RGB')
im1.save(output_pdf)


print("Finished")







##Múltiplas imagens no mesmo PDF
#from PIL import Image
#
#image1 = Image.open(r'C:\Users\Ron\Desktop\Test\image1.png')
#image2 = Image.open(r'C:\Users\Ron\Desktop\Test\image2.png')
#image3 = Image.open(r'C:\Users\Ron\Desktop\Test\image3.png')
#image4 = Image.open(r'C:\Users\Ron\Desktop\Test\image4.png')
# 
#im1 = image1.convert('RGB')
#im2 = image2.convert('RGB')
#im3 = image3.convert('RGB')
#im4 = image4.convert('RGB')
#
#imagelist = [im2,im3,im4]
#
#im1.save(r'C:\Users\Ron\Desktop\Test\myImages.pdf',save_all=True, append_images=imagelist)