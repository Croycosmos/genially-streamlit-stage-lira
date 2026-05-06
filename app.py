import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Stage LIRA",
    layout="wide",
)

st.title("Stage LIRA")

st.markdown(
    """
    Présentation interactive intégrée depuis Genially.
    """
)

GENIALLY_URL = "https://view.genially.com/684a8a004a4c5e03b4857d3b"

components.iframe(
    GENIALLY_URL,
    height=800,
    scrolling=True,
)

with st.sidebar:
    st.header("Contrôles")
    show_genially = st.checkbox("Afficher le Genially", value=True)
    height = st.slider("Hauteur du Genially", 400, 1200, 800, step=50)

    st.divider()
    )

    show_catalogue = st.checkbox("Afficher le catalogue", value=True)

if show_genially:
    st.subheader("Présentation Genially")
    st.iframe(GENIALLY_URL, height=height, width="stretch")

st.divider()

st.subheader("Espace Streamlit")

col1, col2 = st.columns([1, 1])

with col1:
    st.write(f"Traceur sélectionné : **{traceur}**")
    st.write("Ici, on pourra mettre la carte de M31 avec les couches sélectionnables.")

with col2:
    if show_catalogue:
        st.write("Ici, on pourra mettre le tableau des trous HI / traceurs associés.")


