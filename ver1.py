import pyPdf
from pyPdf import PdfFileReader
##pdfOne = PdfFileReader(file( "D:/UC subjects/fall 2015/big data/final project/sample.pdf"))

def getPDFContent(path):
    content = ""
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    print pdf.getNumPages()
    for i in range(0, pdf.getNumPages()):
        content += pdf.getPage(i).extractText() + "\n"
    return content
    
    
text_content = getPDFContent("C:/Users/thiruvengadam/Desktop/python files/DE-1-Information-for-SA.pdf")
text_lower = text_content.lower()
re.split('; |, |\*|\n',text_lower)
print text_lower

import re
phraseRegex=re.compile(r'((\S+\s+){0,4}directed(\S+\s+){0,4}|(\S+\s+){0,4}attention(\s+\S+){0,4})')
mo1=phraseRegex.findall(text_content)
#print mo

phrase_dic = {}
for ele in mo1:
    if ele not in phrase_dic:
        phrase_dic[ele] = 1
    else:
        phrase_dic[ele] = phrase_dic[ele] + 1
#print phrase_dic

