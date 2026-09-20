import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title='Qualímetro',
    page_icon="📊",
    layout="wide"
)

def carregar_css(caminho_css):
    with open(caminho_css, encoding='UTF-8') as arquivo_css:
        st.markdown(
            f"<style>{arquivo_css.read()}</style>",
            unsafe_allow_html=True
        )


caminho_css = Path(__file__).parent / "src" / "style" / "style.css"

carregar_css(caminho_css)

with st.sidebar:
    st.title("Qualímetro")
    st.caption("Relatório de qualidade dos dados")

    st.divider()

    st.subheader("Relatório")
    st.write("- Resumo")

st.caption("Relatório de Qualidade · Nova Análise")

st.title("Comece a análise pelo seu dataset")

st.write(
    """
    Envie o arquivo que deseja 
    analisar a qualidade e estrutura dos dados.
    """
)

st.divider()

col1, col2 = st.columns([1, 2])  # [1,2] são as larguras das colunas

with col1:

    st.subheader("Envie seu arquivo")

    st.write("Selecione o arquivo que deseja analisar.")

    st.write("Formatos aceitos:")
    st.write("- CSV")
    st.write("- Excel")
    st.write("- JSON")

with col2:

    arquivo = st.file_uploader(
        "Selecione o arquivo",
        type=["csv", "xlsx", "json"]
    )

if arquivo is not None:

    st.divider()

    st.success("Arquivo carregado com sucessso!")

    st.subheader("Arquivo selecionado")

    col_nome, col_tipo, col_tamanho = st.columns(3)

    with col_nome:
        st.metric(
            label="Nome",
            value=arquivo.name
        )

    with col_tipo:
        extensao = arquivo.name.split('.')[-1].lower()

        st.metric(
            label="Formato",
            value=extensao
        )

    with col_tamanho:
        tamanho_kb = arquivo.size / 1024

        st.metric(
            label="Tamanho",
            value=f'{tamanho_kb:.2f} KB'
        )

    st.divider()

    analisar = st.button(
        "Gerar diagnóstico",
        type="primary"
    )

    if analisar:

        try:
            extensao = arquivo.name.split('.')[-1].lower()

            if extensao == 'csv':
                dados = pd.read_csv(arquivo)

            elif extensao == 'xlsx':
                dados = pd.read_excel(arquivo)

            elif extensao == 'json':
                dados = pd.read_json(arquivo)

            st.success("Arquivo processado com sucesso!")

            st.subheader("Visão geral")

            col_linhas, col_colunas, col_memoria = st.columns(3)

            with col_linhas:
                st.metric(
                    "Linhas",
                    dados.shape[0]
                )

            with col_colunas:
                st.metric(
                    "Colunas",
                    dados.shape[1]
                )

            with col_memoria:
                memoria_kb = dados.memory_usage(deep=True).sum() / 1024

                st.metric(
                    label="Memória Utilizada",
                    value=f"{memoria_kb:.2f} KB"
                )

            estrutura = pd.DataFrame({
                "Coluna": dados.columns,
                "Tipo": dados.dtypes.astype(str).values
            })

            st.subheader("Estrutura dos Dados")

            st.table(estrutura)

            st.divider()

            st.subheader("Prévia dos dados")

            st.dataframe(
                dados.head(),
                use_container_width=True
            )

        except Exception as erro:
            st.error(f"Não foi possível processar o arquivo {erro}")
