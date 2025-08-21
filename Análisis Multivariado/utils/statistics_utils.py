import numpy as np
import pandas as pd
import random

def generar_datos_aleatorios(n=20, minimo=10, maximo=100):
    return [random.randint(minimo, maximo) for _ in range(n)]

def calcular_tabla_frecuencias(data, intervalos=5):
    serie = pd.Series(data)
    tabla = pd.cut(serie, bins=intervalos).value_counts().sort_index()
    df = pd.DataFrame({"Intervalo": tabla.index.astype(str),
                       "Frecuencia": tabla.values,
                       "Frecuencia Acumulada": tabla.cumsum().values})
    return df.to_html(classes="table table-bordered table-striped", index=False)

def calcular_medidas_posicion(data):
    Q1 = np.percentile(data, 25)
    Q2 = np.percentile(data, 50)
    Q3 = np.percentile(data, 75)
    return Q1, Q2, Q3

def calcular_dispersion(data):
    rango = max(data) - min(data)
    varianza = np.var(data, ddof=1)
    desviacion = np.std(data, ddof=1)
    return rango, varianza, desviacion
