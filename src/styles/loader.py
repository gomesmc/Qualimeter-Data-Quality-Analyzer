from pathlib import Path

import streamlit as st


def carregar_css():

    caminho_css = Path(__file__).parent / "style.css"

    with open(caminho_css, encoding="utf-8") as arquivo_css:

        st.markdown(
            f"<style>{arquivo_css.read()}</style>",
            unsafe_allow_html=True
        )