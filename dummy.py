from gtts import gTTS
import os
from playsound import playsound

import PyPDF2
pdf_file = open('C:/Users/Ajayp/OneDrive/Desktop/project2/song_project.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
print (page_content.encode('utf-8'))
tts = gTTS(text=page_content, lang='en')
tts.save('0.mp3')
os.system("0.mp3")
playsound('0.mp3')

