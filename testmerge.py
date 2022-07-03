
from PyPDF2 import PdfFileWriter, PdfFileReader
input_pdf = PdfFileReader("E:\\求職\\成績單(大學部)-吳俊諺.pdf")
pages=input_pdf.getNumPages()
for i in range(0,pages):
    output = PdfFileWriter()
    output.addPage(input_pdf.getPage(0))
    with open("E:\\求職\\成績單(大學部)-吳俊諺"+str(i)+"pages.pdf", "wb") as output_stream:
        output.write(output_stream)