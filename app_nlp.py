import streamlit as st
import spacy_streamlit

modelos = ["pt_core_news_sm", "pt_core_news_md"]

texto_padrao = "Marck Zuckeberg é o CEO do Facebook"

spacy_streamlit.visualize(modelos, texto_padrao)