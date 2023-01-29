import streamlit as st
import pandas as pd
import zipfile

df = dict()

zf = zipfile.ZipFile('https://drive.google.com/file/d/1R17iOJIqiOsjKeU-cHZtzuCnyRCBgkwJ/view?usp=share_link')
df['2015'] = pd.read_csv(zf.open('2015.csv')); df['2016'] = pd.read_csv(zf.open('2016.csv'));
df['2017'] = pd.read_csv(zf.open('2017.csv')); df['2018'] = pd.read_csv(zf.open('2018.csv'))
df['2019'] = pd.read_csv(zf.open('2019.csv')); df['2020'] = pd.read_csv(zf.open('2020.csv'))
df['2021'] = pd.read_csv(zf.open('2021.csv')); df['2022'] = pd.read_csv(zf.open('2022.csv'))

st.write(df['2015'])
st.write(df['2022'])
