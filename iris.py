import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


def ui_parametros():
    sepal_length = st.sidebar.slider("Sepal length", 4.3, 7.9, 5.0)
    sepal_width = st.sidebar.slider("Sepal width", 2.0, 4.4, 3.2)
    petal_length = st.sidebar.slider("Petal length", 1.0, 6.9, 2.5)
    petal_width = st.sidebar.slider("Petal width", 0.1, 2.5, 0.5)

    data = {
        'sepal_length' : sepal_length,
        'sepal_width' : sepal_width,
        'petal_length' : petal_length,
        'petal_width' : petal_width
    }

    parametros = pd.DataFrame(data, index=[0])
    return parametros


st.header("Iris Flower Prediction App")
st.sidebar.header("UI parametros")
df = ui_parametros()
st.write(df)

# aprendizado supervisionado com informações rotuladas
iris = datasets.load_iris()
# dados independentes
x = iris.data
# dados de previsão
y = iris.target

# classificador de floresta aleatorio
rfc = RandomForestClassifier()
# para realizar o treinamento do modelo
rfc.fit(x, y)

previsao = rfc.predict(df)
# retornar tambem um indice probabilistico
previsao_prob = rfc.predict_proba(df)

st.subheader("Rótulos de classificação")
# classes referentes ao numero retornado
st.write(iris.target_names)
st.subheader("Previsão")
st.write(previsao)
st.subheader("Previsão de percentual")
st.write(previsao_prob)
