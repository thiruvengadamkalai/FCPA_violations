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
    
text_content_lower_add = " "
import re
text_content = getPDFContent("D:/UC subjects/fall 2015/big data/final project/DE-1-Information-for-Grid.pdf")    

text_lower = text_content.lower()
text_content_lower = re.split('; |, |\*|\n',text_lower)
for element in text_content_lower:
   text_content_lower_add = text_content_lower_add + element
#print text_content_lower_add
##
##fine(imposed)?
##· violates(this)?agreement|violation(of)?agreement
##· vacation(of)?conviction
##· withdrawal(of)?plea
##· waiver(of)?appellate
##· (criminal)?fine
##· united states code(section)?
##· special assessment
##· gross pecuniary gain (resulting| from)?offense
##· satisfy(applicable)?burden of proof
##· culpability score
##· accept(ance of responsibility for)?criminal conduct
##· sentence hearing
##· corrupt(conduct)?
##· bribe(ery)?(scheme)?
##· (nature)?(seriousness)?offense
##· bribe payments
##

import re
phraseRegex=re.compile(r'((\S+\s+){0,4} violates(this)?agreement|violation(of)?agreement(\S+\s+){0,4}|(\S+\s+){0,4}vacation(of)?conviction(\s+\S+){0,4}|(\S+\s+){0,4}withdrawal(of)?plea(\s+\S+){0,4} \|(\S+\s+){0,4}waiver(of)?appellate(\s+\S+){0,4}|(\S+\s+){0,4}criminal(\s+\S+){0,4}|(\S+\s+){0,4}united states code(\s+\S+){0,4} \|(\S+\s+){0,4}special assessment(\s+\S+){0,4}|(\S+\s+){0,4}gross pecuniary gain (resulting| from)?offense(\s+\S+){0,4}|(\S+\s+){0,4}satisfy(applicable)?burden of proof(\s+\S+){0,4} \
|(\S+\s+){0,4}culpability score(\s+\S+){0,4}|(\S+\s+){0,4}accept(\s+\S+){0,4}|(\S+\s+){0,4}sentence hearing(\s+\S+){0,4} \
|(\S+\s+){0,4}corrupt(conduct)?(\s+\S+){0,4}|(\S+\s+){0,4}bribe(ery)?(scheme)?(\s+\S+){0,4}|(\S+\s+){0,4}(nature)?(seriousness)?offense(\s+\S+){0,4})')
mo1=phraseRegex.findall(text_content_lower_add)
print mo1
phrase_dic = {}
for ele in mo1:
  if ele not in phrase_dic:
     phrase_dic[ele] = 1
  else:
     phrase_dic[ele] = phrase_dic[ele] + 1
print phrase_dic