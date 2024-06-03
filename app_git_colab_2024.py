
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Herramientas 2024 digitales en español', page_icon='favicon.jpg')
# st.write('↖ Categorias')
st.image('Logo.jpg')
st.title('Herramientas digitales 2024 en español')


categorias = ['research-assistant',
 'translators',
 'presentations',
 'video-editing',
 'video-generators',
 'text-to-video',
 'prompt-generators',
 'writing-generators',
 'storyteller',
 'copywriting-assistant',
 'website-builders',
 'marketing',
 'finance',
 'project-management',
 'social-media',
 'design-generators',
 'image-generators',
 'image-editing',
 'text-to-image',
 'workflows',
 'ai-agents',
 'portrait-generators',
 'image-to-image',
 'avatar-generator',
 'audio-editing',
 'text-to-speech',
 'music-generator',
 'transcriber',
 'students',
 'code-assistant',
 'no-code']

finance=pd.read_csv('finance')


st.table(finance.iloc[0:10])
st.dataframe(finance)

