from PDFExtract import extractPDFText, getPageText, prepareCSV, writeSentencesIntoCSV

pages = extractPDFText('raw_data/minutes.pdf')

CSVRows = ['Sentence', 'Label']

for i in range(len(pages)):
    prepareCSV(CSVRows, 'sentences_' + str(i))
    writeSentencesIntoCSV(pages[i],'sentences_' + str(i))
