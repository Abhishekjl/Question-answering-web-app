import PyPDF2
import re
import os
import warnings
warnings.filterwarnings('ignore')
def document_reader(folder_name):
    text = ""
    for filename in os.listdir(folder_name):
        filepath = os.path.join('docs', filename)
        if filename.split('.')[-1] == 'pdf':
            try:
                file = open(filepath, 'rb')
                fileReader = PyPDF2.PdfFileReader(file)
                page = fileReader.numPages
                for i in range(page):
                    pdf_obj = fileReader.getPage(i)
                    text = text + (pdf_obj.extractText())
            except:
                pass
        else:
            with open(filepath) as f:
                contents = f.read()
                text  = text + contents

            
    text = re.sub(r"[\s \n\*&)($%#+=<>]+"," ", text)
    return text
# with open('text.txt','w', encoding='utf-8') as f:
#     f.write(text)

