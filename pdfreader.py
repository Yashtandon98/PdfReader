import PyPDF2
import pyttsx3
import os
import sys

narrator = pyttsx3.init()
rate = narrator.setProperty('rate', 150)

file = open(r'Path of the file', 'rb')
read = PyPDF2.PdfFileReader(file)
tpage = read.getNumPages()
page = read.getPage(0)
content = page.extractText()

narrator.say(content)
narrator.runAndWait()
