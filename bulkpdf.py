import os
import sys

wordDocsPath = os.path.abspath(sys.argv[1])
pdfFilePath = os.path.abspath(sys.argv[2])

allFiles = os.listdir(wordDocsPath)
entries = []
for file in allFiles:
    if file.endswith("docx"):
        entries.append(file)

os.system("venv\Scripts\\activate")

for entrie in entries:
    xString = "python topdf.py " + "\"" + wordDocsPath + "/" + entrie + "\" \"" + pdfFilePath + "/" + entrie.replace(
        ".docx", ".pdf") + "\""
    print(f"working on {entrie}")
    os.system(xString)

print("done creating pdfs")
print("merging pdfs now")

xString = "python pdfMerger.py " + "\"" + pdfFilePath + "\""
os.system(xString)
