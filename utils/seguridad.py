import streamlit as st
import streamlit_authenticator as stauth

def configurar_autenticacion():
    """Lee los secretos y configura la lectura de cookies de sesión."""
    # Extraer y desvincular los secretos
    credenciales_crudas = st.secrets["credentials"]
    credenciales = {
        "usernames": {
            usuario: dict(datos) 
            for usuario, datos in credenciales_crudas["usernames"].items()
        }
    }

    # Instanciar el autenticador (ESTO ES LO QUE LEE LA COOKIE AUTOMÁTICAMENTE)
    autenticador = stauth.Authenticate(
        credenciales,
        "sellboard_cookie_segura",       
        "esta_es_una_clave_super_secreta_y_muy_larga_de_32_bytes", 
        cookie_expiry_days=30            
    )
    return autenticador