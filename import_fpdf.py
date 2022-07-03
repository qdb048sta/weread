from PIL import Image
from PyPDF2 import PdfFileMerger
from PDFNetPython3.PDFNetPython import PDFDoc, Optimizer, SDFDoc, PDFNet
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
bookstore=["wechat","當當"]
for book in bookstore:
    file_m_folder="D:\\截圖用電子書\\"+book+"\\"
    import os
    print(file_m_folder)
    os.chdir(file_m_folder)
    print(os.listdir())
    counter=0
    for i in os.listdir():
        if "desk" not in i and counter<1:
            os.chdir(file_m_folder+i)
            os.mkdir(file_m_folder+i+"_pdf")
            os.mkdir(file_m_folder+i+"_compressedjpg")

            #compress jpg
            imagelist=os.listdir()
            imagelist.sort()
            textfile1 = i+'_OCR1.txt'
            textfile3= i+ '_OCR3.txt'
            for img in imagelist:
                image = Image.open(img)
                rgb_im=image.convert('L')
                img = Image.open(k)
                '''config1=r'--oem 1'
                config3=r'--oem 3'
                text1 = pytesseract.image_to_string(img, lang='chi_sim',config=config1)
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
                f.close()'''
                rgb_im.save(file_m_folder+i+"_compressedjpg\\"+img[0:33]+"_jpg.jpg", compress_level=9,optimize=True, quality=10)
            print(i,"pdf compressed successful")


            #compressco
            os.chdir(file_m_folder+i+"_compressedjpg") 
            compresslist=os.listdir()
            compresslist.sort()
            compresspage=[]
            compresscover=Image.open(compresslist[0])
            for compress in compresslist:
                compress1 = Image.open(compress)
            
                compresspage.append(compress1)
                compress1.save(file_m_folder+i+"_pdf\\"+compress[0:33]+"_pdf.pdf")
                counter=counter+1
            pdf_filename =file_m_folder+i+"_quadpdf.pdf"
            compresscover.save(pdf_filename, "PDF" ,resolution=50.0, save_all=True, append_images=compresspage,quality=10)
            print(i,"pdf printed successful")
            
            #merge pdf
            os.chdir(file_m_folder+i+"_pdf")
            pdflist=os.listdir()
            pdflist.sort()
            merger=PdfFileMerger()
            for pdf in pdflist:
                merger.append(pdf)

            merger.write(i+"_pdf.pdf")
            merger.write(file_m_folder+i+"_pdf.pdf")
            merger.close()
            os.remove(file_m_folder+i+"_compressedjpg")
            os.remove(file_m_folder+i+"_pdf")      
            print(i,"converted successful")
        counter=counter+1
    