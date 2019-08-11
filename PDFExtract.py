import PyPDF2
import re

def extractPDFText(filePath=''):
    #Open the pdf file in read binary mode.
    fileObject = open(filePath, 'rb')
    
    # Create a pdf reader .
    pdfFileReader = PyPDF2.PdfFileReader(fileObject)
    
    # Get total pdf page number.
    totalPageNumber = pdfFileReader.numPages
    
    # Print pdf total page number.
    print('This pdf file contains totally ' + str(totalPageNumber) + ' pages.')
    
    currentPageNumber = 0
    text = ''
    
    firstPageText = pdfFileReader.getPage(1).extractText()
    
    firstPageText = " ".join(re.split("\s+", firstPageText, flags=re.UNICODE))
    sentenceArray = firstPageText.split('.')
    
    print(sentenceArray)    
   