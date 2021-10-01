import PyPDF2
import os
import sys

pdfFilePath = os.path.abspath(sys.argv[1])


allFiles = os.listdir(pdfFilePath)
pdfFiles = []
for file in allFiles:
    if file.endswith(".pdf"):
        pdfFiles.append(file)

# read all pages of all documents
pdfReaders = []
openFiles = []
for file in pdfFiles:
    openFile = open(pdfFilePath+"/"+file, "rb")
    pdfReaders.append(PyPDF2.PdfFileReader(openFile))

# create pdf-writer
pdfWriter = PyPDF2.PdfFileWriter()

# append all pages to writer
for pdfReader in pdfReaders:
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutputFile = open(pdfFilePath+"/MergedFiles.pdf", "wb")
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
for file in openFiles:
    file.close()
