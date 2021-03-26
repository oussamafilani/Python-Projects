files = ['f1.pdf', 'f2.py' ,'f3.xpdf', 'pdf.txt']


pdfs = [e for e in files if '.pdf' in e]

print(pdfs)
