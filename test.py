import re
import docx
doc = docx.Document('D://py//doc//python02_31_03.docx')
p_li = doc.paragraphs


for p in p_li:
    card = re.sub(r'(?<=-\d)(\d+)(?=\d)', r'******', p.text)
    p.text = card
doc.save('D://py//doc//python02_31_03.docx')