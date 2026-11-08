import streamlit as st

st.set_page_config(
    page_title="OBRA360 | Gestão de Obras",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stApp {
    background-color: #F3F5F8;
}
header[data-testid="stHeader"] {
    background: transparent;
}
.block-container {
    padding-top: 2rem;
}
h1, h2, h3 {
    color: #172B40;
}
div.stButton > button {
    background-color: #172B40;
    color: white;
    border-radius: 8px;
    border: none;
    min-height: 42px;
}
div.stButton > button:hover {
    background-color: #D6A44D;
    color: #172B40;
}
</style>
""", unsafe_allow_html=True)

if "pagina" not in st.session_state:
    st.session_state.pagina = "Dashboard"

with st.sidebar:
    st.markdown("# 🏗️ OBRA360")
    st.caption("GESTÃO INTELIGENTE DE OBRAS")
    st.divider()

    st.markdown("### MENU PRINCIPAL")

    paginas = [
        "Dashboard",
        "Empresas",
        "Obras",
        "Diário de Obra (RDO)",
        "Mão de Obra",
        "Equipamentos",
        "Materiais",
        "Medições",
        "Relatórios",
        "Usuários"
    ]

    for pagina in paginas:
        if st.button(pagina, key=f"menu_{pagina}", use_container_width=True):
            st.session_state.pagina = pagina
            st.rerun()

st.title("🏗️ OBRA360")
st.caption("Plataforma de Gestão de Obras e Engenharia Civil")

st.divider()

pagina = st.session_state.pagina

if pagina == "Dashboard":
    st.subheader("Painel Administrativo")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Empresas", "0")
    col2.metric("Obras ativas", "0")
    col3.metric("RDOs enviados", "0")
    col4.metric("Medições", "0")

    st.info("Bem-vindo ao OBRA360. Cadastre sua primeira empresa para começar.")

elif pagina == "Empresas":
    st.subheader("Cadastro de Empresas")
    st.text_input("Razão social")
    st.text_input("CNPJ")
    st.text_input("Responsável")
    st.text_input("E-mail")
    st.button("Cadastrar empresa")

elif pagina == "Obras":
    st.subheader("Cadastro de Obras")
    st.text_input("Nome da obra")
    st.text_input("Endereço")
    st.text_input("Engenheiro responsável")
    st.date_input("Data de início")
    st.button("Cadastrar obra")

else:
    st.subheader(pagina)
    st.info("Módulo preparado para desenvolvimento.")

st.divider()
st.caption("OBRA360 © 2026 | Gestão profissional de obras")
