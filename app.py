# import packages
from PyPDF2 import PdfReader
import pyttsx3

speaker = pyttsx3.init()

pdfReader = PdfReader(open("Company Law (1).pdf","rb"))
# print(len(pdfReader.pages))
# print(pdfReader.pages[0].extract_text(0))
# text =""
# for page_num in range(len(pdfReader.pages)):
#     text += pdfReader.pages[page_num].extract_text()
#     # speaker.say(text)
#     # speaker.runAndWait()

# # speaker.stop()

# speaker.save_to_file(text, "Enterpreneurship-Notes.mp3")
# speaker.runAndWait()

#============== ingore headers and footers================
page = pdfReader.pages[1]

parts = []

def visitor_body(text, cm, tm, fontDict, fontSize):
    y=tm[5]
    if y>10 and y< 720:
        parts.append(text)
        
page.extract_text(visitor_text=visitor_body)
text_body = "".join(parts)

#print(text_body)
speaker.say(text_body)
speaker.runAndWait()