#firstly intall pdf2docx: pip install pdf2docx
from pdf2docx import Converter 


cv = Converter('Bianka_Pearson.pdf')
cv.convert('test.docx', start=0, end=None)
cv.close()  