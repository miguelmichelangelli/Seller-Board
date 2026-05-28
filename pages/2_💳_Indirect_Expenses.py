import streamlit as st
import PyPDF2
from services.claude_agent import extraer_datos_factura
from utils.seguridad import configurar_autenticacion

st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"] ul li:first-child {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 1. Recuperar el guardia de seguridad
autenticador = configurar_autenticacion()

# 2. Forzar la lectura de la cookie
# Si la cookie es válida, esto no dibuja nada y te da paso.
try:
    autenticador.login()
except Exception as e:
    pass

# 3. Validar si la memoria recuperó el acceso
if not st.session_state.get("authentication_status"):
    # Si no hay cookie o expiró, lo enviamos de vuelta a la entrada al instante
    st.switch_page("app.py")

# --- A PARTIR DE AQUÍ, EL USUARIO ESTÁ 100% VERIFICADO ---
st.title("🧾 Procesamiento de Facturas")
st.write("Sube las facturas de tus proveedores. La IA extraerá los costos automáticamente.")
st.markdown("---")

# 4. SUBIDA DE ARCHIVO
archivo_pdf = st.file_uploader("Arrastra o selecciona tu factura en PDF", type=["pdf"])

# 5. LÓGICA DE PROCESAMIENTO
if archivo_pdf is not None:
    st.success("¡Archivo cargado con éxito!")
    
    # Extraer texto del PDF
    lector = PyPDF2.PdfReader(archivo_pdf)
    texto_factura = ""
    for pagina in lector.pages:
        texto_factura += pagina.extract_text()
        
    # El botón ahora siempre está visible porque la API Key ya está segura en la bóveda
    if st.button("✨ Extraer Costos con IA"):
        with st.spinner("Claude está analizando la factura..."):
            
            # Llamamos a nuestro servicio aislado pasándole ÚNICAMENTE el texto
            resultado = extraer_datos_factura(texto_factura)
            
            if resultado["exito"]:
                st.info(resultado["datos"])
            else:
                st.error(f"Hubo un error de conexión: {resultado['error']}")