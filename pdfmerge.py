import PyPDF2

pdfiles=["1.pdf","2.pdf"] #Enter your pdf file names and their extensions
merger=PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile=open(filename,'rb') #rb=Read Binary
    pdfReader=PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('Merged.pdf') #Enter new pdf file name and its extension