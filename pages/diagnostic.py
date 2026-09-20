import streamlit as st

from src.styles.loader import carregar_css


st.set_page_config(
    page_title="Diagnóstico | Qualímetro",
    page_icon="📊",
    layout="wide"
)

carregar_css()


# ==================================================
# VERIFICA SE EXISTE DATASET
# ==================================================

if "dados" not in st.session_state:

    st.warning("Nenhum dataset foi carregado.")

    if st.button("Voltar para nova análise"):
        st.switch_page("app.py")

    st.stop()


# ==================================================
# RECUPERA OS DADOS
# ==================================================

dados = st.session_state["dados"]

nome_arquivo = st.session_state.get(
    "nome_arquivo",
    "Dataset"
)

total_linhas = dados.shape[0]
total_colunas = dados.shape[1]

# Valores ausentes
total_ausencias = dados.isna().sum().sum()

# Registros duplicados
total_duplicatas = dados.duplicated().sum()

# Total de células do dataset
total_celulas = total_linhas * total_colunas

# Completude
if total_celulas > 0:
    completude = (
        (total_celulas - total_ausencias)
        / total_celulas
    ) * 100
else:
    completude = 0


# Unicidade
if total_linhas > 0:
    unicidade = (
        (total_linhas - total_duplicatas)
        / total_linhas
    ) * 100
else:
    unicidade = 0

# Score inicial de qualidade
score_qualidade = (
    completude + unicidade
) / 2

score_qualidade = round(score_qualidade)
completude = round(completude)


def barra_qualidade(valor):

    valor = max(
        0,
        min(100, int(valor))
    )

    st.markdown(
        f"""
        <div class="barra-qualidade">
            <div class="barra-qualidade__preenchimento" style="width: {valor}%;"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

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
    "RELATÓRIO DE QUALIDADE · DIAGNÓSTICO"
)

st.title(
    f"Diagnóstico de {nome_arquivo}"
)

st.write(
    "Confira os principais indicadores de estrutura "
    "e qualidade do dataset enviado."
)

st.divider()


# ==================================================
# ESTRUTURA VISUAL DO DIAGNÓSTICO
# ==================================================

total_ausencias = dados.isna().sum().sum()

col1, col2 = st.columns(
    [1, 2],
    gap="large"
)


# Card da esquerda
with col1:

    with st.container(border=True):

        st.caption("QUALIDADE GERAL")

        st.metric(
            label="Score",
            value=f"{score_qualidade} / 100"
        )

        barra_qualidade(score_qualidade)

        st.caption(
            "Score calculado a partir de completude e unicidade."
        )


# Card da direita
with col2:

    with st.container(border=True):

        metric1, metric2, metric3, metric4 = st.columns(4)

        with metric1:
            st.metric(
                "Linhas",
                dados.shape[0]
            )

        with metric2:
            st.metric(
                "Colunas",
                dados.shape[1]
            )

        with metric3:
            st.metric(
                "Ausências",
                total_ausencias
        )

        with metric4:
            st.metric(
                "Duplicatas",
                total_duplicatas
            )

        st.divider()

        st.caption(
            "Completude do dataset"
        )

        barra_qualidade(completude)


# ==================================================
# PRÉVIA
# ==================================================

st.divider()

st.subheader(
    "Prévia do dataset"
)

st.dataframe(
    dados.head(),
    use_container_width=True
)


# import streamlit as st

# from src.styles.loader import carregar_css


# st.set_page_config(
#     page_title="Diagnóstico | Qualímetro",
#     page_icon="📊",
#     layout="wide"
# )

# carregar_css()


# # ---------------------------------------------------
# # VERIFICA SE EXISTE UM DATASET NA SESSÃO
# # ---------------------------------------------------

# if "dados" not in st.session_state:

#     st.warning("Nenhum dataset foi carregado.")

#     if st.button("Voltar para nova análise"):
#         st.switch_page("app.py")

#     st.stop()


# # ---------------------------------------------------
# # RECUPERA OS DADOS DA SESSÃO
# # ---------------------------------------------------

# dados = st.session_state["dados"]

# nome_arquivo = st.session_state.get(
#     "nome_arquivo",
#     "Dataset"
# )

# with st.sidebar:

#     st.title("Qualímetro")

#     st.caption(
#         "Relatório de qualidade de dados"
#     )

#     st.divider()

#     st.page_link(
#         "app.py",
#         label="Nova análise"
#     )

#     st.page_link(
#         "pages/diagnostic.py",
#         label="Diagnóstico"
#     )

#     st.divider()


# st.caption(
#     "RELATÓRIO DE QUALIDADE · DIAGNÓSTICO"
# )

# st.title(
#     "Diagnóstico de qualidade"
# )

# st.write(
#     f"Arquivo em análise: {nome_arquivo}"
# )

# st.divider()

# st.subheader("Prévia do dataset")

# st.dataframe(
#     dados.head(),
#     use_container_width=True
# )
