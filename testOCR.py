path="C:\\Users\\starg\\AppData\\Local\\MurGeeScreenshots\\capture_wechat"
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
import os
poppler_path = r"C:\\Users\\starg\\Downloads\\Release-22.01.0-0\\poppler-22.01.0\\Library\\bin"
os.chdir(path)
textfile0="test_txtverutf.txt"
textfile1="test_txtvergbk2312.txt"
textfile2="test_txtverhz.txt"


for i in os.listdir():
    if ".png" in i:
        img = Image.open(i)
        config0=r'--oem 1'
        text0 = pytesseract.image_to_string(img,lang="chi_sim",config=config0)
        f=open(textfile0,"a",encoding='UTF-8')
        f.write("\n")
        f.write("page"+str(i))
        print(text0)
        f.write(text0)
        print("finish"+i)
        f.close()

        f=open(textfile1,"a",encoding='gbk2312')
        f.write("\n")
        f.write("page"+str(i))
        print(text0)
        f.write(text0)
        print("finish"+i)
        f.close()

        f=open(textfile1,"a",encoding='hz')
        f.write("\n")
        f.write("page"+str(i))
        print(text0)
        f.write(text0)
        print("finish"+i)
        f.close()
    