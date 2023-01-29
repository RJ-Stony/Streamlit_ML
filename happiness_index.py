import streamlit as st
import pandas as pd
from zipfile import ZipFile
import streamlit.components.v1 as components

df = dict()

def activate_sidebar():
    with st.sidebar:
        uploaded_files = st.file_uploader('CSV 파일 혹은 ZIP 파일을 업로드해주세요.', accept_multiple_files=True)
    # Check if files were uploaded
    if len(uploaded_files) > 0:
        for uploaded_file in uploaded_files:
            # If zip file, extract contents
            if uploaded_file.type == 'application/x-zip-compressed':
                zf = ZipFile(uploaded_file)
                df['2015'] = pd.read_csv(zf.open('2015.csv')); df['2016'] = pd.read_csv(zf.open('2016.csv'));
                df['2017'] = pd.read_csv(zf.open('2017.csv')); df['2018'] = pd.read_csv(zf.open('2018.csv'))
                df['2019'] = pd.read_csv(zf.open('2019.csv')); df['2020'] = pd.read_csv(zf.open('2020.csv'))
                df['2021'] = pd.read_csv(zf.open('2021.csv')); df['2022'] = pd.read_csv(zf.open('2022.csv'))

                st.write(df['2015'])
                st.write(df['2022'])

            elif uploaded_file.type == 'text/csv':
                uploaded_df = pd.read_csv(uploaded_file)
                st.write(uploaded_df)

activate_sidebar()

for key in df:
    st.title(key + ' Columns')
    col_df = pd.DataFrame(df[key].columns, columns='Columns')
    st.dataframe(col_df)
