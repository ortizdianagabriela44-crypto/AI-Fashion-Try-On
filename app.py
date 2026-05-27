import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image

# Inicializar MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True)

def superponer_prenda(usuario_img, prenda_img):
    # Convertir a formato utilizable por OpenCV
    usuario_np = np.array(usuario_img)
    prenda_np = np.array(prenda_img)
    
    # Procesar con MediaPipe
    results = pose.process(usuario_np)
    
    if results.pose_landmarks:
        # Extraer puntos de los hombros (Landmarks 11 y 12)
        h, w, _ = usuario_np.shape
        hombro_izq = results.pose_landmarks.landmark[11]
        hombro_der = results.pose_landmarks.landmark[12]
        
        # Calcular ancho de hombros
        ancho_hombros = int(abs(hombro_izq.x - hombro_der.x) * w)
        
        # Redimensionar la prenda al ancho de hombros
        ancho_prenda = ancho_hombros + 50 # Un poco de margen
        escala = ancho_prenda / prenda_np.shape[1]
        nuevo_alto = int(prenda_np.shape[0] * escala)
        prenda_resized = cv2.resize(prenda_np, (ancho_prenda, nuevo_alto))
        
        # Aquí iría la lógica de pegado (Alpha Blending)
        # Por ahora, devolvemos el aviso de que el motor está detectando correctamente
        return True, "¡Éxito! Hombros detectados. Prenda ajustada al ancho."
    
    return False, "No se detectaron hombros claramente."

# --- Interfaz Streamlit ---
st.title("👗 AI Fashion Try-On")
foto_usuario = st.file_uploader("Sube tu foto", type=['jpg', 'png'])
foto_prenda = st.file_uploader("Sube la prenda", type=['jpg', 'png'])

if st.button("Probar Prenda"):
    if foto_usuario and foto_prenda:
        img_u = Image.open(foto_usuario)
        img_p = Image.open(foto_prenda)
        
        exito, mensaje = superponer_prenda(img_u, img_p)
        
        if exito:
            st.success(mensaje)
            st.image(img_u) # En el futuro, aquí mostrarás img_u con la prenda encima
        else:
            st.error(mensaje)
