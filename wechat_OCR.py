from PIL import Image
import pytesseract
from pdf2image import convert_from_path
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
import os
poppler_path = r"C:\\Users\\starg\\Downloads\\Release-22.01.0-0\\poppler-22.01.0\\Library\\bin"
from PyPDF2 import PdfFileWriter, PdfFileReader

#from PyPDF2 import PdfFileReader, PdfFileWriter
os.chdir("D:\\scannedOCR\\")
from datetime import datetime
counter=0
filename=os.listdir()
filename.sort(reverse=True)
for k in filename:
    if counter>=0:


        print(datetime.now())
        if "quadpdf" in k:
            name=k.split("_")[0]+"_quad"
        else:
            name=k.split("_")[0]
        if name+"_splitpdf" not in os.listdir():
            os.mkdir(name+"_splitpdf")
        if name+"_splitjpg" not in os.listdir():
            os.mkdir(name+"_splitjpg")
        print(k)
        print(os.getcwd())


        input_pdf = PdfFileReader(k)
        pages=input_pdf.getNumPages()
        for i in range(0,pages):
            output = PdfFileWriter()
            output.addPage(input_pdf.getPage(i))
            with open(name+"_splitpdf\\"+"pdf_page"+str(i), "wb") as output_stream:
                output.write(output_stream)
            images=convert_from_path(name+"_splitpdf\\"+"pdf_page"+str(i),poppler_path=poppler_path)
            images[0].save(name+"_splitjpg\\"+"jpg_page"+str(i)+".jpg","JPEG")
            print("now on converted "+k+" page number "+str(i))
        
        print("starting OCR"+k)
        #textfile0=name+"_txtver0.txt"
        textfile1="D:\\scannedOCR\\"+name+"_txtver1.txt"
        #textfile2=name+"_txtver2.txt"
        textfile3="D:\\scannedOCR\\"+name+"_txtver3.txt"
        os.chdir(name+"_splitjpg\\")
        jpglistraw=os.listdir()
        jpgdict={}
        for jpgr in jpglistraw:
            jpgdict[int(jpgr[8:].split(".")[0])]=jpgr
        jpglist=[]
        for jpgd in jpgdict:
            jpglist.append(int(jpgd))
        jpglist.sort()
        #print(jpgdict)
        for jpg in jpglist:
            print(str(jpg))
            img = Image.open(jpgdict[jpg])
            print("now on OCR"+k+" "+str(jpg))

            #config0=r'--oem 0'
            config1=r'--oem 1'
            #config2=r'--oem 2'
            config3=r'--oem 3'

            #text0 = pytesseract.image_to_string(img, lang='chi_sim',config=config0)
            text1 = pytesseract.image_to_string(img, lang='chi_sim',config=config1)
            #text2 = pytesseract.image_to_string(img, lang='chi_sim',config=config2)
            text3 = pytesseract.image_to_string(img, lang='chi_sim',config=config3)


            f=open(textfile1,"a",encoding='UTF-8')
            f.write("\n")
            f.write("page"+str(jpg))
            f.write(text1)
            f.close()



            f=open(textfile3,"a",encoding='UTF-8')
            f.write("\n")
            f.write("page"+str(jpg))
            f.write(text3)
            f.close()
            print("OCR finished"+ str(jpg))

        print("successful write "+name)
        print(datetime.now())
    counter=counter+1

        