import streamlit as st
from st_audiorec import st_audiorec

st.set_page_config(page_title="Asistente de Contingencia", page_icon="🎙️", layout="centered")

st.title("🎙️ Asistente de Voz - Contingencia")
st.write("Graba tu audio para procesarlo y registrarlo.")

# Sección de Grabación de Voz
st.subheader("1. Grabación de Audio")
wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    # Muestra el reproductor del audio grabado
    st.audio(wav_audio_data, format='audio/wav')
    st.success("¡Audio grabado exitosamente!")

# Sección de Texto / Notas
st.subheader("2. Registro de Texto")
texto_nota = st.text_area("Edita o complementa el texto aquí antes de guardar:", placeholder="El texto transcrito o tus notas aparecerán aquí...")

# Botón para simular la acción de guardar o preparar para documento
if st.button("Procesar y Guardar"):
    if texto_nota.strip() != "":
        st.success("¡Texto registrado correctamente para exportar!")
        # Aquí puedes agregar la lógica para generar el archivo o procesar
    else:
        st.warning("Por favor, ingresa o genera texto para continuar.")
