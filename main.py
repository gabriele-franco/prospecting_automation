import streamlit as st
import pandas as pd
from func import classify_website, add_prefixes,convert_df,extract_company_name



csv=st.file_uploader('upload your csv', type='csv')
if csv:

    data=pd.read_csv(csv)

    urls = add_prefixes(data["domain"])
    contents=[]
    subjects=[]
    for i in urls:
        message, subject=classify_website(i)
        contents.append(message)
        subjects.append(subject)

    data['subject']=subjects
    data['email']=contents

    st.download_button(
    "Press to Download",
    convert_df(data),
    file_name='large_df.csv',
    mime='text/csv')






