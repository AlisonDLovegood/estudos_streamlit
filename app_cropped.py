import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image

st.title("Cortar imagem")
img_file = st.sidebar.file_uploader(label="Envie uma imagem:", type=["jpg", "png", "jpeg"])
realtime_update = st.sidebar.checkbox("Atualização automática", value=True)

box_color = st.sidebar.color_picker(label="Grupo de cores", value='#0400FF')

# grupo de codigo referente ao radio
aspect_choice = st.sidebar.radio(label="Proporção da Tela", options=["1:1","16:9", "4:3"])
aspect_dict = {
	"1:1":(1,1),
	"16:9":(16,9),
	"4:3":(4,3)
}
aspect_ratio = aspect_dict[aspect_choice]

if img_file:
    imagem = Image.open(img_file)
    # por padrao o cropped atualiza automaticamente, caso nao:
    if not realtime_update:
        st.write("Duplo clique para cortar a imagem")

    imagem_cortada = st_cropper(imagem, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)

    st.text("Resultado:")
    corte = imagem_cortada.thumbnail((350,350))
    st.image(imagem_cortada)