# bulk_pdf
commandline tools to merge a lot of word documents to one big pdf

# Usage
This section explains how to use these tools
## bulkpdf.py
```python
python bulkpdf.py inputDir outputDir
```
combines the functionality of both topdf.py and pdfMerger.py to create a merged pdf inside the directory `outputDir` from .docx files in the inputdirectory `inputDir`

## todpf.py
```python
python topdf.py input output
```
converts an `input` file (.docx word document) into a pdf `output` file

## pdfMerger.py
```python
python pdfMerger.py inputDir
```
merges pdf files from `inputDir` to an output pdf inside the same directory
