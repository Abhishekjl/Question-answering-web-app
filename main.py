import streamlit as st
import PyPDF2
from read_files import document_reader
import os
from os import listdir
from os.path import isfile, join





def save_uploaded_file(uploadedfile):
  with open(os.path.join("docs",uploadedfile.name),"wb") as f:
     f.write(uploadedfile.getbuffer())

def file_uploader():
    uploaded_file = st.sidebar.file_uploader('prefer .txt file')
    if uploaded_file is not None:
        save_uploaded_file(uploaded_file)

        text =  document_reader('docs')        
        return text



st.sidebar.title('NLP tasks')


option  = st.sidebar.selectbox(
    'upload',[
        'Upload Document',
        'Copy paste document'
    ]
)



if option == 'Upload Document':
    document = file_uploader()
    st.text_area("document", value=document, height=60, max_chars=None, key=None)

    files = os.listdir('docs')
    for f in files:
        try:
            os.remove(os.path.join('docs',f))
        except:
            pass

    
        
if option == 'Copy paste document':
    document = st.text_area(label = 'paste your text')

task  = st.sidebar.selectbox(
    'select option',[
        'None',
        'Question Answering', 
        'Text Summarization'
    ]
)

if task == 'Question Answering':
    question = st.text_area(label = 'Write your Question')

    QA_input = {
    'question': question,
    'context': document
}
    
    import transformers
    from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
    model_name = "distilbert-base-uncased-distilled-squad"
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    res = nlp(QA_input)
    st.write(f"Answer: {res['answer']}")
