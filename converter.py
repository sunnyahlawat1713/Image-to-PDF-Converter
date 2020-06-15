# Necessary imports
import img2pdf
from PIL import Image
import os

# Case 1: If the user wants to store every image in a separate PDF
def single_image_per_pdf():
    i = 0

    while True:
        file_path = str(input("Enter the full path of the file :"))

        if file_path == "Stop":
            break

        else:
            i += 1 
            img_path = file_path
            img = Image.open(img_path)
            pdf_bytes = img2pdf.convert(img.filename)
            pdf_path = f'C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/file{i}.pdf'
            file = open(pdf_path, 'wb')
            file.write(pdf_bytes)
            img.close()
            file.close()
            print("Successfully made pdf file!!")
            #print(i)

# Case 2: If the user wants to save multiple images in one PDF
def multiple_images_per_pdf():

    list_of_addresses = []
    im_list = []

    pdf_name = str(input("Enter the desired name of the pdf file: "))
    num_files = int(input("Enter the number of pictures required in the PDF"))

    for i in range(num_files):
        ele = str(input("Enter the path of the file"))
        list_of_addresses.append(ele)

    for i in range(len(list_of_addresses)):
        im_list.append(Image.open(list_of_addresses[i]))

    pdf_path = f'C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/{pdf_name}.pdf'

    im_list[0].save(pdf_path, "PDF", resolution = 100.0,save_all = True,
    append_images = im_list[1:])

choice = input("Enter 1 for 1 image pdfs, 2 for multiple image pdfs")

# Program initiating code
if choice == '1':
    single_image_per_pdf()
elif choice == '2':
    multiple_images_per_pdf()
else:
    print("try again")

    

        

        
