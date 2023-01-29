import streamlit as st

with st.sidebar:
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)

for uploaded_file in uploaded_files:
    if uploaded_file is not None:
        uploaded_df = pd.read_csv(uploaded_file)
    st.write(uploaded_df)
