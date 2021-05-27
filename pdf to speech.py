import PyPDF2  #module for reading pdf file
import pyttsx3  #module for speech engine

#Opening the pdf file
pdf_file=open('story.pdf','rb')  #story.pdf is the name of the pdf file

#reading pdf file
pdf_reader=PyPDF2.PdfFileReader(pdf_file)

print(pdf_reader.numPages)
#Initialization of speaker
speaker=pyttsx3.init()

#setting the page
page=pdf_reader.getPage(0)

#extracting the text from selected page
text=page.extractText()

#passing the text to speaker to say
speaker.say(text)

#it will process the voice command
speaker.runAndWait()