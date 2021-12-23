import PyPDF2

pdfFileObj = open('automate the boring stuff with python automate the boring stuff with python ( PDFDrive ).pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages