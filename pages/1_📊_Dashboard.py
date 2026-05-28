import streamlit as st
import pandas as pd
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
st.title("📊 Dashboard")
st.markdown("---")

# 3. MÉTRICAS PRINCIPALES (Reemplazando el HTML y CSS antiguo)
# Usamos st.columns para separar las tarjetas de forma responsiva
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Today")
    st.metric(label="Sales", value="€ 825.06")
    st.write("**Net profit:** -€ 945.23")

with col2:
    st.subheader("Yesterday")
    st.metric(label="Sales", value="€ 9,761.93")
    st.write("**Net profit:** -€ 2,122.96")

with col3:
    st.subheader("Month to date")
    st.metric(label="Sales", value="€ 184,031.54", delta="-5.8%")
    st.write("**Net profit:** € 9,586.08")

st.markdown("---")

# 4. TABLA DE DESGLOSE DE PRODUCTOS
st.subheader("📋 Rendimiento por Producto (Hoy)")

# Datos de ejemplo basados en tu código original
datos_productos = {
    "Product / SKU": [
        "PACK 2 UNIDADES ZZ Coopermatic...",
        "MENFORSAN Pipetas Anti-Insectos...",
        "COMPO BIO Triple Acción...",
        "Pack 2 uds. Dodot Extra Absorción..."
    ],
    "Units sold": [3, 3, 2, 2],
    "Sales": ["€ 85.03", "€ 22.02", "€ 20.96", "€ 79.90"],
    "Net profit": ["€ 3.65", "-€ 0.07", "-€ 0.64", "€ 10.68"],
    "ROI": ["9%", "-1%", "-10%", "30%"]
}

df_productos = pd.DataFrame(datos_productos)

# st.dataframe() renderiza la tabla de forma interactiva
st.dataframe(df_productos, use_container_width=True, hide_index=True)