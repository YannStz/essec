import streamlit as st
from constants import * 

def download_template(template_file=TEMPLATE_FILE):
    content_file = open(template_file,'r')
    content = content_file.read()
    st.download_button('The first step is to fill the CV. Download the template here :rocket:', content)  # Defaults to 'text/plain'
    content_file.close()
    

def download_result(template_file=RESULT_FILE):
    content_file = open(template_file,'r')
    content = content_file.read()
    st.download_button('Download the result of your AI improved CV here :wink:', content)  # Defaults to 'text/plain'
    content_file.close()

def experience_parser(text_cv):
    list_experiences = text_cv.split('EXPERIENCE ')
    selected_experience = []
    for l in list_experiences:
        try:
            int(l[0][0])
            selected_experience.append(l)
        except:
            continue
    return selected_experience
