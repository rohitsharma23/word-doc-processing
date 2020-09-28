import textract
import time
import docx2txt

#read a docx file
text = textract.process("data/cv.docx")
string_decoded = str(text.decode("utf-8"))
f = open('./results/'+time.strftime("read_docx_%Y_%m_%d-%H_%M_%S")+'.txt', 'w', newline='', encoding="utf-8")
f.write(string_decoded)
f.close()

#read a .doc file
my_text = docx2txt.process("data/cv.doc")
f = open('./results/'+time.strftime("read_doc_%Y_%m_%d-%H_%M_%S")+'.txt', 'w', newline='', encoding="utf-8")
f.write(string_decoded)
f.close()