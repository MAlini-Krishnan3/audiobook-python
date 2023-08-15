# audiobook-python
This is a small python code that will read a PDF file on your local machine out aloud, like an audiobook.

Libraries used- PyPDF2, pyttsx3

Install these libraries if you haven't already using pip:
  pip install pyttsx3
  pip install PyPDF2
  
Note: If you come across an error 'AttributeError: 'super' object has no attribute 'init'', then please do the following:
1. pip install pyobjc
2. open this file /usr/local/lib/python3.11/site-packages/pyttsx3/drivers/nsss.py and change the following lines of code
     #self = super(NSSpeechDriver, self).init() comment this line, and add the following
     self = objc.super(NSSpeechDriver, self).init()
