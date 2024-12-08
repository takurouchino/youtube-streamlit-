import streamlit as st
import pandas as pd

st.title('streamlit 超入門')

st.write('DatafFrame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40],
})

st.write(df)
