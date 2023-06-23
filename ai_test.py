import openai
import urllib.request
from PIL import Image
import streamlit as st

openai.api_key = ""

def gerar_imagem(descricao):
    response = openai.Image.create(
        prompt=descricao,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    urllib.request.urlretrieve(image_url, "img.png")
    imagem = Image.open("img.png")
    return imagem

st.title("Gerar Imagens com DALL-E")
descricao_img = st.text_input("Descreva a Imagem")

if st.button("Gerar Imagem"):
    imagem = gerar_imagem(descricao_img)
    st.image(imagem)