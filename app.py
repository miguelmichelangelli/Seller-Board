import streamlit as st
from utils.seguridad import configurar_autenticacion

st.set_page_config(page_title="Sellboard - Acceso", page_icon="🔐", layout="centered")

# 1. Llamar al guardia de seguridad (Lee la cookie si existe)
autenticador = configurar_autenticacion()

# 2. Renderizar el Login visualmente
autenticador.login()

# 3. Lógica de acceso (Ya no usamos la variable inventada 'acceso_concedido')
if st.session_state.get("authentication_status") is False:
    st.error("⚠️ Usuario o contraseña incorrectos")

elif st.session_state.get("authentication_status") is None:
    st.markdown(
        '''<style>[data-testid="collapsedControl"], [data-testid="stSidebar"] { display: none; }</style>''',
        unsafe_allow_html=True
    )
    st.title("Bienvenido a Sellboard 🚀")
    st.warning("Por favor, inicia sesión para continuar.")

elif st.session_state.get("authentication_status"):
    st.markdown(
        '''<style>[data-testid="stSidebarNav"] ul li:first-child { display: none; }</style>''',
        unsafe_allow_html=True
    )
    
    st.success(f"¡Bienvenido {st.session_state.get('name')}! 🔓")
    st.write("Usa el menú lateral para navegar por los módulos.")
    
    autenticador.logout("Cerrar Sesión", "main")