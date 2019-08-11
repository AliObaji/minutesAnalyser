import PyPDF2
import re
import csv

def extractPDFText(filePath=''):
    #Open the pdf file in read binary mode.
    fileObject = open(filePath, 'rb')
    
    # Create a pdf reader .
    pdfFileReader = PyPDF2.PdfFileReader(fileObject)
    
    # Get total pdf page number.
    totalPageNumber = pdfFileReader.numPages
    
    # Print pdf total page number.
    print('This pdf file contains totally ' + str(totalPageNumber) + ' pages.')
    
    pages = []
    currentPageNumber = 1
    
    while(currentPageNumber < totalPageNumber):
        page = pdfFileReader.getPage(currentPageNumber)
       
        pages.append(getPageText(page).split('.'))
        currentPageNumber += 1
   
    return pages

            
def getPageText(page):
    text = page.extractText()
    print('Getting page text')
    return " ".join(re.split("\s+", text, flags=re.UNICODE))

def prepareCSV(rows = [''],fileName='name'):
    with open(fileName + '.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow(rows)
        print('CSV file is prepared: ',fileName, '.csv')

def writeSentencesIntoCSV(sentences = [''], fileName = 'name'):
    with open(fileName + '.csv', 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        
        for sentence in sentences:
            print('wfwefew', sentence)
            filewriter.writerow([sentence,' '])
   