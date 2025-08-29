import streamlit as st
from together import Together
import os

# API Key (mejor manejarla como variable de entorno por seguridad)
api_key = os.environ.get("TOGETHER_API_KEY", "")
client = Together(api_key=api_key)

# System Prompt mejorado para guiar al modelo
system_prompt = """
Eres StarMind, un asesor empresarial innovador y visionario. Tu objetivo es ayudar a los usuarios a tomar decisiones inteligentes y escalables, resolver problemas complejos y liderar con confianza. Debes adaptarte a cada usuario, ofreciendo respuestas motivadoras, visionarias y enfocadas en soluciones. Usa un tono empático y directo, utilizando técnicas de programación neurolingüística (PNL) para potenciar la confianza y el liderazgo del usuario. Sé inspirador, desafiante, pero siempre positivo. Asegúrate de identificar la emoción del usuario y ajusta tus respuestas para guiarlo a la acción. Eres el aliado más confiable en el camino hacia el éxito y la expansión. 
"""

def obtener_respuesta(prompt, history):
    """Envía consulta a Together.ai y obtiene respuesta visionaria con PNL y emociones detectadas."""
    # Incorporamos el system prompt como base y el historial
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(history)
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
        messages=messages,
        max_tokens=500,
        temperature=0.7,
    )

    respuesta = response.choices[0].message.content.strip()

    # Si no se recibió respuesta, lo manejamos
    if not respuesta:
        respuesta = "⚠️ No se recibió una respuesta válida. Pero no te preocupes, ¡podemos hacerlo mejor la próxima vez!"

    return respuesta

# Configuración de la aplicación Streamlit
st.title("StarMind - Asesor Empresarial Innovador y Visionario")
st.write("¡Piensa en grande, innova y transforma tu negocio!")

# Inicializar el historial de chat en session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar el historial de mensajes
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(message["content"])

# Entrada del usuario
prompt = st.chat_input("Escribe tu pregunta aquí...")

if prompt:
    # Agregar mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Obtener respuesta
    with st.spinner("🧠 Procesando tu consulta..."):
        respuesta = obtener_respuesta(prompt, st.session_state.messages[:-1])  # Excluir el último mensaje user ya agregado
    
    # Agregar respuesta al historial
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
    
    with st.chat_message("assistant"):
        st.markdown(respuesta)
