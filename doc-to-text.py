import textract
import time
text = textract.process("data/cv.docx")
string1 = str(text.decode("utf-8"))

f = open('./results/'+time.strftime("read_docx_%Y_%m_%d-%H_%M_%S")+'.txt', 'w', newline='', encoding="utf-8")
f.write(string1)
f.close()