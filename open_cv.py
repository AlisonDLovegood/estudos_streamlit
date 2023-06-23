import streamlit as st
import cv2
from PIL import Image
import numpy as np
from skimage import morphology, io, color, feature, filters

def brilho_imagem(imagem, resultado):
    imagem = cv2.convertScaleAbs(imagem, beta=resultado)
    return imagem


def borrar_imagem(imagem, resultado):
    imagem = cv2.GaussianBlur(imagem, (7,7), resultado)
    return imagem


def melhorar_detalhes(imagem):
    imagem = cv2.detailEnhance(imagem, sigma_s=34, sigma_r=0.5)
    return imagem


# praticar conversão de imagem colorida para escala de cinza, saindo de canal rgb para escalar
def escala_cinza(imagem):
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    return imagem

def principal():
    st.title("OpenCV Data App")
    st.subheader("Processamento de imagens com a biblioteca OpenCV")
    st.text("Streamlit com OpenCV")

    # img = cv2.imread("assets/mew.jpg")
    img = st.file_uploader("Envie sua imagem", type=["jpg", "png", "jpeg"])

    taxa_borrao = st.sidebar.slider("Borrão", min_value=0.0, max_value=3.5, value=0.0)
    qtd_brilho = st.sidebar.slider("Brilho", min_value=-50.0, max_value=50.0, value=0.0)
    filtro_aprimoramento = st.sidebar.checkbox("Melhorar imagem")
    filtro_cinza = st.sidebar.checkbox("Converter para escala de cinza")
    # skimage é mais prático de trabalhar n precisa de func
    filtro_erosao = st.sidebar.checkbox("Filtro de erosão")
    filtro_dilatação = st.sidebar.checkbox("Filtro de dilatação")
    filtro_edge = st.sidebar.checkbox("Filtro de edge")

    if not img:
        return None
    
    imagem_original = Image.open(img)
    # a imagem precisa ser trabalhada como base em array para trabalhar com todas as funções
    imagem_original = np.array(imagem_original)

    imagem_processada = borrar_imagem(imagem_original, taxa_borrao) #aqui se espera uma imagem em array
    imagem_processada = brilho_imagem(imagem_processada, qtd_brilho)
    if filtro_aprimoramento:
        imagem_processada = melhorar_detalhes(imagem_processada)
    if filtro_cinza:
        imagem_processada = escala_cinza(imagem_processada)
    if filtro_erosao:
        imagem_processada = morphology.erosion(imagem_processada)
    if filtro_dilatação:
        imagem_processada = morphology.dilation(imagem_processada)
    if filtro_edge:
        imagem_processada = filters.sobel(imagem_processada)


    col1, col2 = st.columns(2)
    with col1:
        st.text("Imagem original:")
        st.image(imagem_original)
    with col2:
        st.text("Imagem com alteração:")
        st.image(imagem_processada)


if __name__ == '__main__':
    principal()



# img = cv2.imread("assets/mew.jpg")

# img_processada = melhorar_detalhes(img)

# cv2.imshow("Imagem original", img)
# cv2.imshow("Imagem Alterada", img_processada)

# cv2.waitKey(0)
# cv2.destroyAllWindows()