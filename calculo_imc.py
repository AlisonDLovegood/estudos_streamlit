import streamlit as st

st.title("Calculadora de IMC")

peso = st.number_input("Digite o seu peso (em kg):")
st.markdown("<br>", unsafe_allow_html=True)
status = st.radio("Selecione a opção de altura:", ('Centímetros', 'Metros'))

if status == 'Centímetros':
    altura = st.number_input("Digite a sua altura:")
    try:
        imc = peso / ((altura /100)**2)
    except ValueError as e:
        print("Erro:", str(e))
else:
    altura = st.number_input("Digite a sua altura:")
    try:
        imc = peso / (altura ** 2)
    except:
        st.warning("Insira algum valor de peso!")

st.markdown("<br>", unsafe_allow_html=True)
if altura and peso:
    if (st.button('Calcular IMC')):
        st.text(f"Seu índice de IMC é: {imc:.2f}")
        if(imc < 16):
            st.error("Você está EXTREMAMENTE abaixo do peso!")
        elif (imc >= 16 and imc < 18.5):
            st.warning("Você está ABAIXO do peso!")
        elif (imc >= 18.5 and imc < 25):
            st.success("Você está SAUDÁVEL!")
        elif (imc >= 25 and imc < 30):
            st.warning("Você está com EXCESSO de peso!")
        elif (imc >= 30):
            st.error("Você está ACIMA do peso!")