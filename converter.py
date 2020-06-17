# Necessary imports
import img2pdf
from PIL import Image
import os
import pytesseract
import cv2
from fpdf import FPDF

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'



# IMAGE EDITING

def image_editor():
    file_path = str(input('Enter the full path of the file : '))
    img = Image.open(file_path)
    editing_choice = str(input("Enter 1 if you want to resize image, 2 if you want to rotate it, 3 if you want it convert it to greyscale: "))
    if editing_choice == '1':
        size = int(input("Enter the required dimension: "))
        img_size = (size, size)
        img.thumbnail(img_size)
        img.save("C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/ie_1.jpg")
    elif editing_choice == '2':
        angle = int(input("Enter the angle in degrees you want it rotated by(add minus sign for clockwise): "))
        print(angle)
        img.rotate(angle).save('C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/ie_1.jpg')
    elif editing_choice == '3':
        img.convert(mode = "L").save('C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/ie_1.jpg')


    



# Case 1: If the user wants to store every image in a separate PDF
def single_image_per_pdf():
    i = 0

    while True:
        file_path = str(input("Enter the full path of the file(Enter 'Stop' to terminate):  "))

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
    num_files = int(input("Enter the number of pictures required in the PDF: "))

    for i in range(num_files):
        ele = str(input("Enter the path of the file: "))
        list_of_addresses.append(ele)

    for i in range(len(list_of_addresses)):
        im_list.append(Image.open(list_of_addresses[i]))

    pdf_path = f'C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/{pdf_name}.pdf'

    im_list[0].save(pdf_path, "PDF", resolution = 100.0,save_all = True,
    append_images = im_list[1:])




# Case 3: If the user wants to scan the text from an image and store it in a pdf.

# Case3A: The user wants to upload the image from their computer.
def text_to_pdf():
    img_path = str(input("Enter full image path: "))
    img = cv2.imread(f"{img_path}")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = pytesseract.image_to_string(img)
    #cv2.imshow("Result", img)

    #cv2.waitKey(0)
    pdf_path = str(input("Enter the desired name of the pdf file: "))
    with open(f'C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/{pdf_path}.txt',mode ='w') as file:      
        file.write(result) 
        #print(result) 

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size = 15)

    f = open(f'C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/{pdf_path}.txt', 'r')

    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1, align = "C")

    pdf.output(f"C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/{pdf_path}.pdf")



# Case 4:The user wants to capture an image from the camera of the laptop.
def capture_image():
    print("When the camera feed opens, press 'Space' to take a picture and press 'Esc' to end the process!")
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/opencv_frame_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()




def single_image_per_pdf2():
    file_path = f"C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/opencv_frame_{0}.jpg"
    img_path = file_path
    img = Image.open(img_path)
    pdf_bytes = img2pdf.convert(img.filename)
    pdf_path = 'C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/file.pdf'
    file = open(pdf_path, 'wb')
    file.write(pdf_bytes)
    img.close()
    file.close()
    print("Successfully made pdf file!!")




def multiple_images_per_pdf2():
    list_of_addresses = []
    im_list = []

    pdf_name = str(input("Enter the desired name of the pdf file: "))
    num_files = int(input("Enter the number of pictures required in the PDF: "))

    for i in range(num_files):
        ele = f"C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/opencv_frame_{i}.jpg"
        list_of_addresses.append(ele)

    for i in range(len(list_of_addresses)):
        im_list.append(Image.open(list_of_addresses[i]))

    pdf_path = f'C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/{pdf_name}.pdf'

    im_list[0].save(pdf_path, "PDF", resolution = 100.0,save_all = True,
    append_images = im_list[1:])




def text_to_pdf2():
    img_path = f"C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/opencv_frame_{0}.jpg"
    img = cv2.imread(f"{img_path}")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = pytesseract.image_to_string(img)
    #cv2.imshow("Result", img)

    #cv2.waitKey(0)
    pdf_path = str(input("Enter the desired name of the pdf file: "))
    with open(f'C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/{pdf_path}.txt',mode ='w') as file:      
        file.write(result) 
        #print(result) 

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size = 15)

    f = open(f'C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/{pdf_path}.txt', 'r')

    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1, align = "C")

    pdf.output(f"C:/Users/Sunny Ahlawat/Desktop/Tantrabyte/img2pdf/{pdf_path}.pdf")


    



# Program initiating code

choice = input("Enter 1 for 1 image pdfs, 2 for multiple image pdfs, 3 for converting image text to PDF, 4 for capturing image now, and 5 for editing the image: ")
if choice == '1':
    single_image_per_pdf()
elif choice == '2':
    multiple_images_per_pdf()
elif choice == '3':
    text_to_pdf()
elif choice == '4':
    capture_image()
    sub_choice = (input("Press 1 to create 1 image pdf, 2 to create multiple image pdf, and 3 to scan text from image and store it in a pdf: "))
    if sub_choice == '1':
        single_image_per_pdf2()
    elif sub_choice == '2':
        multiple_images_per_pdf2()
    elif sub_choice == '3':
        text_to_pdf2()
elif choice == '5':
    image_editor()
else:
    print("Try again please...")





    

        

        
