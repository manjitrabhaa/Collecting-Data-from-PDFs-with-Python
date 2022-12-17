# import PyPDF2
# a = PyPDF2.PdfFileReader("yourfile.pdf")
# print(a.documentInfo)
# print(a.getNumPages())
# print(a.getPage(2).extract_text())
# str = ""
# for i in range("From","To"):
#     str += a.getPage(i).extract_text()
# with open("text.txt", "w", encoding="utf-8") as f:
#     f.write(str)


import PyPDF2
from PyPDF2 import PdfFileReader
#Creating a pdf file object
pdf = open("yourfile","rb")
#creating pdf reader object
pdf_reader = PyPDF2.PdfFileReader(pdf)
#checking number of pages in a pdf file
print(pdf_reader.numPages)
#creating a page object
page = pdf_reader.getPage()
#finally extracting text from the page
print(page.extractText())
#closing the pdf file
pdf.close()
