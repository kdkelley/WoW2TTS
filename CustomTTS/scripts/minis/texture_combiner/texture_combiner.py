import sys
import os
import math
from PIL import Image

#put customTTS's path in the ""
#you will have to add a second '\' character wherever a single '\' character appears
customTTSPATH = ""

temp_path = customTTSPATH + "\\minis\\temp"

temp_files = os.listdir(temp_path)

print("temp files:",temp_files)

image_names = []

for file in temp_files:
    if file[-3:] == "png" and file != "one.png":
        image_names.append(temp_path + "\\" +  file)

print("image names:",image_names)
num_images = len(image_names)

images = list(map(Image.open, image_names))
widths, heights = zip(*(i.size for i in images))

images.sort(key=lambda x: x.size[0], reverse=True)

max_width = max(widths)
max_height = max(heights)

print("max width pre adjust:", max_width)
print("max height pre adjust:", max_height)

total_height = sum(heights)

print("total height pre adjust:",total_height)

total_height = int(math.pow(2,math.ceil(math.log(total_height,2))))
max_width = int(math.pow(2,math.ceil(math.log(max_width,2))))

print("max width post adjust:",max_width)
print("total height post adjust:",total_height)

new_im = Image.new('RGBA', (max_width, total_height))

y_base = 0
for im in images:
    x_offset = math.ceil((max_width - im.size[0]) / 2)
    y_offset = y_base
    print("x off:",x_offset)
    print("y off:",y_offset)
    new_im.paste(im, (x_offset, y_offset))
    y_base += im.size[1]

new_im.save(temp_path + '\\one.png')
