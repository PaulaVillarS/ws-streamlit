import streamlit as st

st.image('https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png')
st.title('Introducción a Streamlit - Workshop')
st.markdown('***')

st.sidebar.markdown('Introducción sobre los usos y ventajas de Streamlit')

st.markdown('## ¿Qué es y para qué sirve streamlit?')
st.markdown('''
Streamlit es una librería que permite crear `aplicaciones web` para Data Science y Machine Learning de forma rápida y sin necesidad de saber otro lenguaje de programación, debido a que son `desarrolladas puramente en Python`.

Es compatible con las librerías más usadas en esta área, como Numpy, Pandas, Matplotlib, Seaborn, Scikit-Learn, Keras, PyTorch, etc.
''')

st.markdown('## ¿Por qué Streamlit?')
st.markdown('''
Para tener un `dashboard en Python` necesitamos unir la manipulación de datos con la visualización, e incorporar interacción con el usuario.

Para poder hacer esta unión sin tener que utilizar código específico para la creación de páginas webs, existen las `librerías Streamlit y Dash`. Ambas brindan un servicio para construir aplicaciones webs a través de datos trabajados en Python pero Stremlit, a diferencia de dash, no requiere experiencia en temas front-end (como CSS, Html u otro lenguaje) ni necesita grandes servidores de almacenamiento.

Por esto, se recomienda utilizar Streamlit en proyectos en los cuales se necesite crear dashboards de forma `rápida, sencilla y sólo con lenguaje Python`. 
''')

st.markdown('***')
st.write('## Material complementario')
st.markdown('[Documentación Streamlit](https://docs.streamlit.io/library/api-reference)')
st.markdown('[Uso Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)')
