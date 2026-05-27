import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI Fashion Try-On", layout="wide")

st.title("👗 AI Fashion Try-On Platform")
st.markdown("### Vístete virtualmente y reduce el desperdicio textil")

col1, col2 = st.columns(2)

with col1:
    st.header("1. Sube tus fotos")
    foto_usuario = st.file_uploader("Foto de cuerpo entero", type=['jpg', 'jpeg', 'png'])
    foto_prenda = st.file_uploader("Imagen de la prenda", type=['jpg', 'jpeg', 'png'])
    
    st.header("2. Tus medidas")
    altura = st.number_input("Altura (cm)", min_value=100, max_value=250, value=170)
    boton_generar = st.button("Generar Prueba Virtual", type="primary")

with col2:
    st.header("Resultado IA")
    if boton_generar:
        if foto_usuario and foto_prenda:
            st.success("¡Imágenes recibidas! El módulo de IA está listo.")
            st.image(foto_usuario, caption="Tu foto", use_container_width=True)
            st.info("💡 Talla recomendada: Calculando con MediaPipe...")
        else:
            st.warning("Por favor, sube ambas imágenes.")
