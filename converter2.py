from PIL import Image

import os


i = 0
while True:
    num_files = str(input("Enter the full path of the file :"))
    if num_files == "Stop":
        break
    else:
        filename = num_files
        im = Image.open(filename)
        if im.mode == "RGBA":
            im  = im.convert("RGB")
        new_filename = f'C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/file{i}.pdf'
        if not os.path.exists(new_filename):
            im.save(new_filename, "PDF", resolution = 100.0)
            print("PDF successfully created")
    i += 1






'''
filename = 'C:/Users/Sunny Ahlawat/Pictures/Saved Pictures/mclaren_mso_675lt_gulf_racing_theme_2018_4k_8k-3840x2160.jpg'

im = Image.open(filename)

if im.mode == "RGBA":
    im = im.convert("RGB")

new_filename = 'C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/file2.pdf'
if not os.path.exists(new_filename):
    im.save(new_filename, "PDF", resolution = 100.0)
'''
