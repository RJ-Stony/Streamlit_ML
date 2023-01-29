import streamlit as st
import pandas as pd
from zipfile import ZipFile
import streamlit.components.v1 as components

df = dict()

zf = ZipFile('https://github.com/RJ-Stony/Streamlit_ML/blob/e3b30c59cd3f8e9c0909d34943d6dc394b141f0a/archive.zip?raw=true')
df['2015'] = pd.read_csv(zf.open('2015.csv')); df['2016'] = pd.read_csv(zf.open('2016.csv'));
df['2017'] = pd.read_csv(zf.open('2017.csv')); df['2018'] = pd.read_csv(zf.open('2018.csv'))
df['2019'] = pd.read_csv(zf.open('2019.csv')); df['2020'] = pd.read_csv(zf.open('2020.csv'))
df['2021'] = pd.read_csv(zf.open('2021.csv')); df['2022'] = pd.read_csv(zf.open('2022.csv'))
            
st.write(df['2015'])
st.write(df['2022'])
            
