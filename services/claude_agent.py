import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')

def extraer_datos_factura(texto_factura):
    """
    Envía el texto crudo de la factura a Claude y devuelve los datos estructurados.
    La API Key se obtiene automáticamente de los secretos de Streamlit.
    """
    try:
        # Extraemos la llave directamente de la bóveda
        cliente = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
        
        prompt = f"""
        Eres un asistente contable experto. Analiza el siguiente texto de una factura PDF y extrae estos datos exactos:
        - Nombre del Proveedor
        - Número de Factura o Albarán
        - Importe Total (con su moneda)
        
        Devuelve ÚNICAMENTE los datos en una lista clara. No agregues saludos.
        
        Texto de la factura:
        {texto_factura}
        """
        
        respuesta = cliente.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return {"exito": True, "datos": respuesta.content[0].text}
        
    except Exception as e:
        return {"exito": False, "error": str(e)}