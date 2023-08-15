#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyttsx3
import PyPDF2

def initializePDFReader(pdfPath):
    pdfBook = open(pdfPath, 'rb') #reading the pdf as a binary book
    global pdfReader, audioOutput
    pdfReader = PyPDF2.PdfReader(pdfBook)
    audioOutput = pyttsx3.init()
    

def readFunction(pageNumber):
    page = pdfReader.pages[pageNumber]  #page numbers are indexed from 0 to n-1
    text = page.extract_text()
    audioOutput.say(text)
    audioOutput.runAndWait()

def readPDF(lowerPageNo, upperPageNumber):
    if(lowerPageNo == upperPageNumber):
        readFunction(lowerPageNo - 1)    #only one page is read
    else:
        for page in range(lowerPageNo - 1, upperPageNumber):
            readFunction(page)


def displayFunction():
    try:
        pdfUrl = input("Enter the absolute path of the PDF: ")
        initializePDFReader(str(pdfUrl))
    except FileNotFoundError:
        print("File not Found! Please enter the correct path!")
    else:
        numberOfPages = len(pdfReader.pages)

        print('This pdf has {} pages'.format(str(numberOfPages)))

        lowerPage = input("Enter the lower page number index you'd like: ")

        if (int(lowerPage) > 0 and int(lowerPage) <= int(numberOfPages)):
              upperPage = input("Enter the upper page number index you'd like: ")
              if (int(upperPage) >= int(lowerPage) and int(upperPage) <= int(numberOfPages)):
                  readPDF(int(lowerPage), int(upperPage))
              else:
                  print("ERROR! Please enter a valid page number!")
        else:
              print("ERROR! Please enter a valid page number!")
          
#main
displayFunction()
    


# In[ ]:




