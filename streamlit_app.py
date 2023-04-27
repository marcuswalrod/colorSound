import streamlit as st
import pandas as pd
import numpy as np

def foo():
	print('bar')

data = './data.txt'

st.set_page_config(layout='wide')
st.title('I convert art to music.')
st.file_uploader('Upload a file')

col1, col2 = st.columns([1, 1])
data = np.random.randn(10, 1)

with col1:
	st.subheader("Select these certain items")
	st.multiselect('Test', ['item1', 'item2', 'item3'])
	st.multiselect('Test2', ['item1', 'item2', 'item3'])

with col2:
	st.subheader("Select these attributes")
	st.number_input('Pick a number', 0, 10)
	st.number_input('Pick another number', 0, 10)
	