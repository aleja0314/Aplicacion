

import streamlit as st
import numpy as np 

st.title('ANIMALIZE')
st.header('Bienvenido a nuestra aplicación.')

mascota = st.multiselect("¿Que tipo de mascota tienes?", ("Perro","Gato","Pájaro/Canario"))
st.write("Espero que esté muy bien tu mascota, pronto te ayudaremos con él." .format(",".join(mascota)))
wild = st.selectbox("¿Te interesan los animales salvajes?",("Sí, claro.","No, la verdad." ))
wild2 = str(wild)
if wild2 == "Sí, claro.":
    st.write("¡Qué bien! , aquí conocerás sobre ellos")
else:
    st.write("Lástima, porque aquí encontrás cosas sobre ellos.")
    