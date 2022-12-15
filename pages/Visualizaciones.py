import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Definimos las columnas que nos interesan
fields = ['country', 'points', 'price', 'variety']

# Cargamos el DataFrame sólo con esas columnas
df = pd.read_csv('wine_reviews.csv', usecols=fields)
df.dropna(inplace=True)

st.title('Visualizaciones en Streamlit')
st.subheader('Principales componentes')
st.markdown('***')

if st.checkbox('Mostrar DF'):
    st.dataframe(df)

if st.checkbox('Vista de datos (Head o Tail)'):
    if st.button('Mostrar head'):
        st.write(df.head())
    if st.button('Mostrar tail'):
        st.write(df.tail())

st.subheader('Información de dimensiones')

dim = st.radio('Dimensiónm a mostrar:', ('Filas', 'Columnas'),horizontal=True)
if dim == 'Filas':
    st.write('Cantidad de filas:', df.shape[0])
else:
    st.write('Cantidad de columnas:', df.shape[1])

st.markdown('***')
st.header('Visualizaciones')

precio_limite = st.slider('Definir precio máximo',0,4000,1500)

fig = plt.figure(figsize=(6,4))
sns.scatterplot(x= 'price', y = 'points', data=df[df['price']<precio_limite])
st.pyplot(fig)

countries_list = df['country'].unique().tolist()
countries = st.multiselect('Seleccione países a analizar:', countries_list, default=['Argentina','Chile','Spain'])
df_countries = df[df['country'].isin(countries)]
fig = plt.figure(figsize=(6,4))
sns.scatterplot(x= 'price', y = 'points', hue='country', data=df_countries[df_countries['price']<precio_limite])
st.pyplot(fig)

if st.checkbox('Mostrar en dos columnas Argentina y Chile',False):
    col1, col2 = st.columns(2)
    with col1:
        df_countries = df[df['country']=='Argentina']
        fig = plt.figure()
        sns.scatterplot(x= 'price', y='points',data=df_countries[df_countries['price']<precio_limite])
        plt.title('Puntajes según precio para Argentina')
        st.pyplot(fig)
    with col2:
        df_countries = df[df['country']=='Chile']
        fig = plt.figure()
        sns.scatterplot(x= 'price', y = 'points',data=df_countries[df_countries['price']<precio_limite])
        plt.title('Puntajes según precio para Chile')
        st.pyplot(fig)
