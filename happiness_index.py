import streamlit as st
import pandas as pd
import zipfile

with st.sidebar:
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)

with zipfile.ZipFile(uploaded_files, "r") as z:
    z.extractall(".")
    
    if z is not None:
        uploaded_df = pd.read_csv(z)
    st.write(uploaded_df)

    
