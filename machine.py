import os
import PyPDF2
from gtts import gTTS 

def pdf_():
    book = open('./db/main.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    page_content=""
    for page_number in range(0,1):
        page = pdfReader.getPage(page_number)
        page_content += page.extractText()

    final_file = gTTS(text=page_content, lang='en')
    final_file.save(os.path.join(r'X:\Code\Python\pdfify\output\generatedspeech.mp3'))
    
