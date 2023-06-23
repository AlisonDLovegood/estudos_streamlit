import streamlit as st
import yfinance as yf

st.title("Preço de Ativo")
st.header("Informações a Respeito do Fechamento e Volume de Algumas Ações")

opcoes = st.selectbox(
	'Escolha o Ativo',
	('ENBR3.SA', 'BBAS3.SA', 'BBDC4.SA', 'PETR4.SA', 'VALE5.SA'))

tickerSimbolo = opcoes
tickerData = yf.Ticker(tickerSimbolo)

tickerDf = tickerData.history(period='1d', start='2012-5-19', end='2022-5-19')

# Open  #High  #Low  #Close  #Volume  #Dividends  #Stock

st.header("Gráfico de Fechamento")

st.line_chart(tickerDf.Close)

st.header("Gráfico de Volume")

st.line_chart(tickerDf.Volume)

st.header("Gráfico de Dividendos")

st.line_chart(tickerDf.Dividends)