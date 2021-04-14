import PIL
import os
import os.path
from PIL import Image

f = r'c://Users/Kristopher/OneDrive/AISC/IU_dataset/images/images_normalized'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((256,256))
    img.save(f_img)

