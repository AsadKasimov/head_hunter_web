from PyPDF2 import PdfFileReader
import zipfile
import csv
from openpyxl import load_workbook

# тут только запись в файлы

with zipfile.ZipFile('hh_ru/data/spam.zip', 'w') as myzip:
    myzip.write('hh_ru/data/some.csv')
    myzip.write('hh_ru/data/simple_demo.pdf')
    myzip.write('hh_ru/data/test_with_files.xlsx')  # работа с архивированием в zip

with open('hh_ru/data/some.csv', 'w', newline='') as f:
    state_info = ["California", "Sacramento", "Los Angeles", "39538223"]
    writer = csv.writer(f)
    writer.writerow(state_info)  # работа с csv

pdf_document = "hh_ru/data/simple_demo.pdf"
with open(pdf_document, "rb") as filehandle:
    pdf = PdfFileReader(filehandle)
    info = pdf.getDocumentInfo()
    pages = pdf.getNumPages()
    print(f'\n {info}')
    print(f'\nnumber of pages: {pages}\n')  # работа с pdf
