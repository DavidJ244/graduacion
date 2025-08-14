import streamlit as st
import joblib
import numpy as np

# Cargar el modelo entrenado
modelo = joblib.load("primermillon.joblib")

# Configuración de la página
st.set_page_config(page_title="Predictor de Éxito Académico", page_icon="🎓", layout="centered")

# Título y autor
st.title("Predictor de Éxito Académico")
st.subheader("Autor: Profe Alfredo")

# Imagen debajo del autor
st.image("https://buscacarrera.com.co/public/content/articulos/la-clave-del-exito-academico-como-crear-un-plan-de-estudio-efectivo.jpg")

# Introducción
st.write("""
Bienvenido a la aplicación para predecir el éxito académico.  
Para usarla:
1. Ajusta las barras deslizantes según tus valores de **Nota IA** y **GPA** (ambos entre 0.0 y 1.0).
2. Haz clic en el botón para obtener la predicción.
""")

# Sliders de entrada
nota_ia = st.slider("Nota IA", 0.0, 1.0, 0.5, step=0.1)
gpa = st.slider("GPA", 0.0, 1.0, 0.5, step=0.1)

# Botón para predecir
if st.button("Predecir"):
    # Convertir a formato para el modelo
    entrada = np.array([[nota_ia, gpa]])
    prediccion = modelo.predict(entrada)[0]

    # Mostrar resultado
    if prediccion == 0:
        st.markdown("<h3 style='color:red;'>😞 No se graduará</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color:green;'>🎉 Felicitaciones, te vas a graduar con honores</h3>", unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown("© 2025 UNAB")

