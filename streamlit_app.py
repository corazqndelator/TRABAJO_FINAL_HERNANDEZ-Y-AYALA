import streamlit as st

# --- TEMA SPIDER-MAN ---
st.markdown("""
<style>

    /* --- Fondo principal --- */
    .stApp {
        background-color: #7a0e1a !important; /* rojo vino spider-man */
        color: white !important;
        font-family: Arial, Helvetica, sans-serif !important;
    }

    /* --- Sidebar temática spider-man --- */
    [data-testid="stSidebar"] {
        background-color: #0d2c54 !important; /* azul marino */
        color: white !important;
    }

    /* Texto dentro del sidebar */
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Inputs con estilo */
    input, textarea, select {
        background-color: rgba(255,255,255,0.15) !important;
        color: white !important;
    }

    /* Botones tipo spider-man */
    .stButton>button {
        background-color: #0d2c54 !important;   /* azul marino */
        color: white !important;
        border-radius: 6px;
        border: 2px solid #e00000 !important;   /* rojo intenso */
        padding: 8px 16px;
        font-weight: bold;
    }

    .stButton>button:hover {
        background-color: #e00000 !important;   /* rojo spider-man */
        border: 2px solid white !important;
        color: white !important;
    }

    /* NO cambiar el título que ya configuraste tú */
    h1, h2 {
        font-family: inherit !important;
        color: white !important;
    }

</style>
""", unsafe_allow_html=True)

