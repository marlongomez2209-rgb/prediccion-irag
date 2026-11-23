# Predicción de atenciones por infección respiratoria aguda grave (IRAG) en Bucaramanga

## Descripción del proyecto

Este proyecto tiene como finalidad desarrollar un modelo de aprendizaje automático capaz de predecir el comportamiento semanal de las atenciones por infección respiratoria aguda grave (IRAG) en los servicios de consulta externa y urgencias de Bucaramanga.

Para su desarrollo se utiliza un conjunto de datos abiertos de vigilancia epidemiológica, que contiene registros históricos de eventos relacionados con infecciones respiratorias. A partir de estos datos se realiza un proceso de exploración, limpieza, organización y preparación de la información para su posterior análisis.

## Objetivo

Desarrollar una herramienta que permita estimar la cantidad de atenciones semanales por IRAG, utilizando información histórica y técnicas de aprendizaje automático, como apoyo para el análisis y la planificación de los servicios de salud.

## Datos utilizados

- **Fuente:** Datos Abiertos de Colombia (datos.gov.co).
- **Conjunto de datos:** Datos colectivos de infección respiratoria aguda de vigilancia epidemiológica.
- **Periodo de los registros:** 2012–2025.
- **Variable objetivo:** Total de eventos de morbilidad de IRAG por consulta externa y urgencias.
- **Frecuencia de análisis:** Semanal.

## Modelo de aprendizaje automático

Para realizar las predicciones se implementó un algoritmo de **árboles de decisión (Decision Tree Regressor)**, utilizando variables como el año, la semana epidemiológica y los registros de atenciones de semanas anteriores.

El modelo fue entrenado con datos históricos y evaluado mediante las métricas MAE, RMSE y R².

## Tecnologías utilizadas

- Python
- Google Colab
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- GitHub

## Aplicación

El proyecto contempla el desarrollo de una aplicación web mediante Streamlit, que permitirá interactuar con el modelo entrenado y consultar estimaciones de las atenciones semanales por IRAG.

## Alcance y limitaciones

Las predicciones corresponden a estimaciones de atenciones reportadas por consulta externa y urgencias, no al número de personas únicas enfermas ni a la demanda real de medicamentos. Los resultados dependen de la calidad y disponibilidad de los registros históricos y pueden mejorarse mediante ajustes al modelo, nuevas variables y la evaluación de otros algoritmos.

---

**Proyecto académico – Ingeniería Mecatrónica**
