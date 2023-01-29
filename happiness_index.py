import streamlit as st
import pandas as pd
import zipfile

df = dict()

with st.sidebar:
    uploaded_files = st.file_uploader('CSV 파일을 업로드해주세요.', accept_multiple_files=True)

# Check if files were uploaded
if len(uploaded_files) > 0:
    for uploaded_file in uploaded_files:
        # If zip file, extract contents
        if uploaded_file.type == 'application/zip':
            zf = zipfile.ZipFile(uploaded_file)
            df['2015'] = pd.read_csv(zf.open('2015.csv'))
            st.write(df['2015'])
    
        elif uploaded_file.type == 'csv':
            uploaded_df = pd.read_csv(uploaded_file)
            st.write(uploaded_df)
