from PIL import Image
import pytesseract
custom_oem_psm_config = r'--oem 3 --psm 6'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image=Image.open("C:\\Users\\starg\\Pictures\\BlueStacks\\教育心理學理論與實踐\\Screenshot_2022.06.12_12.42.02.413.png")
s=pytesseract.image_to_string(image,lang="chi_sim",config=custom_oem_psm_config)
print(s)