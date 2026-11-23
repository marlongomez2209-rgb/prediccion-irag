import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Predicción de atenciones IRAG",
    page_icon="🏥",
    layout="centered"
)

@st.cache_resource
def cargar_modelo():
    return joblib.load("modelo_arbol_decision_irag.pkl")

modelo = cargar_modelo()

st.title("Predicción de atenciones por IRAG")
st.subheader("Bucaramanga, Colombia")

st.write("""
Esta herramienta utiliza un modelo de aprendizaje automático
basado en árboles de decisión para estimar las atenciones semanales
por infección respiratoria aguda grave (IRAG).
""")

st.divider()

st.header("Datos para realizar la predicción")

st.write("""
Ingresa la información correspondiente a la semana que deseas
analizar y los registros de las semanas anteriores.
""")

with st.form("formulario_prediccion"):

    anio = st.number_input(
        "Año",
        min_value=2012,
        max_value=2035,
        value=2026,
        step=1
    )

    semana = st.number_input(
        "Semana epidemiológica",
        min_value=1,
        max_value=53,
        value=48,
        step=1
    )

    semana_anterior = st.number_input(
        "Atenciones de la semana anterior",
        min_value=0,
        value=3000,
        step=100
    )

    hace_2_semanas = st.number_input(
        "Atenciones de hace 2 semanas",
        min_value=0,
        value=2800,
        step=100
    )

    hace_4_semanas = st.number_input(
        "Atenciones de hace 4 semanas",
        min_value=0,
        value=2600,
        step=100
    )

    promedio_4_semanas = st.number_input(
        "Promedio de atenciones de las 4 semanas anteriores",
        min_value=0.0,
        value=2800.0,
        step=100.0
    )

    boton = st.form_submit_button("Realizar predicción")

if boton:

    datos = pd.DataFrame([{
        "anio": anio,
        "semana_epidemiologica": semana,
        "atenciones_semana_anterior": semana_anterior,
        "atenciones_hace_2_semanas": hace_2_semanas,
        "atenciones_hace_4_semanas": hace_4_semanas,
        "promedio_4_semanas": promedio_4_semanas
    }])

    prediccion = modelo.predict(datos)[0]

    st.divider()
    st.subheader("Resultado de la predicción")

    st.metric(
        "Atenciones estimadas por IRAG",
        f"{max(0, round(prediccion)):,}"
    )

    st.info(
        "Este resultado es una estimación del modelo y no representa "
        "un conteo real ni el número de personas únicas enfermas."
    )
