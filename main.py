import streamlit as st
import pandas as pd
import numpy as np


st.title('Encontrar el código postal válido más cercano')


head_cols = ['codigo_postal', 'estado', 'localidad', 'municipio']
df_codigos = pd.read_excel(
    'data/catalogo_codigo_postal.xlsx', header=None, names=head_cols)

df_codigos = df_codigos.fillna(-1)
df_codigos = df_codigos.astype(
    {'codigo_postal': int, 'localidad': int, 'municipio': int})

with st.form("my_form"):
    st.write("Por favor llena los campos")
    codigo = st.number_input('Código Postal', min_value=None, max_value=None, value=0, step=None,
                             format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
    localidad = st.number_input('Localidad', min_value=None, max_value=None, value=0, step=None,
                                format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
    municipio = st.number_input('Municipio', min_value=None, max_value=None, value=0, step=None,
                                format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)

    df_codigos = df_codigos[(df_codigos['localidad'] == localidad) & (
        df_codigos['municipio'] == municipio)]

    if not df_codigos.empty:
        codigos = np.asarray(df_codigos['codigo_postal'])
        index = (np.abs(codigos - codigo)).argmin()
        closest_value = codigos[index]
    else:
        closest_value = 0

    submitted = st.form_submit_button("Encontrar")
    if submitted:
        if closest_value != 0:
            st.metric('El código postal válido más cercano es',
                      closest_value, delta=None, delta_color="normal")
        else:
            st.metric('Datos incorrectos, por favor verifica',
                      closest_value, delta=None, delta_color="normal")
