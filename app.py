import pandas as pd
import streamlit as st

from src.styles.loader import carregar_css


# ==================================================
# CONFIGURAÇÃO DA PÁGINA
# ==================================================

st.set_page_config(
    page_title="Qualímetro",
    page_icon="📊",
    layout="wide"
)

carregar_css()


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("Qualímetro")

    st.caption(
        "Relatório de qualidade de dados"
    )

    st.divider()

    st.page_link(
        "app.py",
        label="Nova análise"
    )

    st.page_link(
        "pages/diagnostic.py",
        label="Diagnóstico"
    )

    st.divider()


# ==================================================
# CABEÇALHO
# ==================================================

st.caption(
    "RELATÓRIO DE QUALIDADE · NOVA ANÁLISE"
)

st.title(
    "Comece pelo seu dataset"
)

st.write(
    "Envie o arquivo que deseja analisar. "
    "O Qualímetro irá avaliar estrutura, completude, "
    "consistência e qualidade dos dados."
)

st.divider()


# ==================================================
# ÁREA DE UPLOAD
# ==================================================

col1, col2 = st.columns(
    [1, 2],
    gap="large"
)


with col1:

    st.subheader(
        "Envie seu arquivo"
    )

    st.write(
        "Selecione um conjunto de dados "
        "para iniciar o diagnóstico."
    )

    st.caption(
        "FORMATOS ACEITOS"
    )

    st.write("CSV")
    st.write("Excel")
    st.write("JSON")


with col2:

    with st.container(border=True):

        arquivo = st.file_uploader(
            "Selecione ou arraste um arquivo",
            type=[
                "csv",
                "xlsx",
                "json"
            ]
        )

        if arquivo is not None:

            st.success(
                "Arquivo carregado com sucesso!"
            )

            st.write(
                f"**Arquivo:** {arquivo.name}"
            )

            tamanho_kb = arquivo.size / 1024

            st.caption(
                f"Tamanho: {tamanho_kb:.2f} KB"
            )

            analisar = st.button(
                "Gerar diagnóstico",
                type="primary",
                use_container_width=True
            )

            if analisar:

                try:

                    # Identifica a extensão
                    extensao = (
                        arquivo.name
                        .split(".")[-1]
                        .lower()
                    )


                    # ==========================================
                    # LEITURA DO ARQUIVO
                    # ==========================================

                    if extensao == "csv":

                        dados = pd.read_csv(
                            arquivo
                        )


                    elif extensao == "xlsx":

                        dados = pd.read_excel(
                            arquivo
                        )


                    elif extensao == "json":

                        dados = pd.read_json(
                            arquivo
                        )


                    else:

                        st.error(
                            "Formato de arquivo não suportado."
                        )

                        st.stop()


                    # ==========================================
                    # SALVA OS DADOS NA SESSÃO
                    # ==========================================

                    st.session_state["dados"] = dados

                    st.session_state[
                        "nome_arquivo"
                    ] = arquivo.name


                    # ==========================================
                    # REDIRECIONA PARA O DIAGNÓSTICO
                    # ==========================================

                    st.switch_page(
                        "pages/diagnostic.py"
                    )


                except Exception as erro:

                    st.error(
                        "Não foi possível processar "
                        f"o arquivo: {erro}"
                    )