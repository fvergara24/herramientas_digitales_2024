
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Herramientas 2024 digitales en español', page_icon='favicon.jpg')
# st.write('↖ Categorias')
st.image('Logo.jpg')
st.title('Herramientas digitales 2024 en español')

socialmedia=pd.read_csv('social-media.csv')

st.table(socialmedia.iloc[0:10])
