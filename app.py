import streamlit as st
from streamlit_audiorecorder import audiorecorder

st.set_page_config(
    page_title="Asistente de Contingencia - CESFAM",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Asistente de Registro Clínico por Contingencia")
st.markdown("Herramienta rápida para estructurar la consulta y llevarla a la hoja de respaldo de Rayen.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Audio o Texto de la Consulta")
    st.markdown("Puedes grabar la conversación directamente desde tu micrófono:")
    
    # Grabador de audio en el navegador
    audio = audiorecorder("Grabar Audio", "Detener Grabación")
    
    if len(audio) > 0:
        st.audio(audio.export().read())
        st.success("¡Audio capturado con éxito!")

    st.markdown("---")
    st.markdown("O escribe/pega el resumen de la atención:")
    
    texto_ejemplo = (
        "Paciente de 40 años consulta por cefalea tensional de 2 días de evolución. "
        "Al examen físico: sin alteraciones neurológicas agudas, presión arterial normal. "
        "Se indica analgésico y reposo."
    )
    
    texto_ingresado = st.text_area("Notas clínicas de la consulta:", value=texto_ejemplo, height=180)
    
    boton_procesar = st.button("Estructurar para Contingencia", type="primary", use_container_width=True)

with col2:
    st.subheader("2. Formato Oficial (Hoja de Contingencia)")
    st.markdown("Resultado ordenado listo para **copiar y pegar**:")
    
    if boton_procesar:
        with st.spinner("Procesando formato clínico..."):
            
            # Formato estándar listo para el portapapeles
            resultado_final = f"""========================================
HOJA DE CONTINGENCIA - REGISTRO CLÍNICO
========================================

* ANAMNESIS / HISTORIA CLÍNICA:
  {texto_ingresado}

* EXAMEN FÍSICO:
  Evaluación realizada según pauta clínica de contingencia.

* DIAGNÓSTICO / HIPÓTESIS:
  Impresión diagnóstica registrada en atención.

* PLAN / INDICACIONES:
  - Indicaciones médicas entregadas al paciente.
  - Reposo y pauta según corresponda.
"""
            st.code(resultado_final, language="markdown")
            st.success("¡Estructurado con éxito! Ya puedes copiarlo.")
