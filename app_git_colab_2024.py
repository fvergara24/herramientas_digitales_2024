
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

df=pd.read_csv('todos.csv')
#df=df.drop(columns='Unnamed: 0',axis=1)

df_columna1=df.iloc[:round(len(df)/2),:]
df_columna2=df.iloc[round(len(df)/2):,:]

#imagen1=df['Imagenes_url'][0]+'.jpg'

text=st.text_input('Buscar aplicaciones','')
text = text.lower()

if text:
    mask = df['Descripcion'].str.contains(text)
    contador=0
    for i in range(len(mask)):
      if mask.loc[i]==False:
        contador+=1
    if contador==len(mask):
      st.write('No hay coincidencias')
    df_busqueda = df[mask]
    df_busqueda = df_busqueda.reset_index(drop=True)
    for j in range(len(df_busqueda)):
      st.write(f"{[df_busqueda.iloc[j][0]]}(%s)" % df_busqueda.iloc[j][2])
      st.caption(df_busqueda.iloc[j][1])
      #st.image(df_busqueda.iloc[j][3], caption=df_busqueda.iloc[j][3], use_column_width='auto')

else:
    col1, col2= st.columns(2)

    with col1:
      for i in range(len(df_columna1)):
        #original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">f"{[df_columna1.iloc[i][0]]}(%s)" % df_columna1.iloc[i][2]</p>'
        #st.markdown(original_title, unsafe_allow_html=True)
        st.write(f"{[df_columna1.iloc[i][0]]}(%s)" % df_columna1.iloc[i][2])
        st.caption(df_columna1.iloc[i][1])
        #st.image(df_columna1.iloc[0][3], caption=df_columna1.iloc[0][3], use_column_width='auto')

    with col2:
      for i in range(len(df_columna2)):
        st.write(f"{[df_columna2.iloc[i][0]]}(%s)" % df_columna2.iloc[i][2])
        st.caption(df_columna2.iloc[i][1])
        #st.image(df_columna2.iloc[1][3], caption=df_columna2.iloc[1][2])
