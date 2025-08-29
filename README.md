# Streamlit Chatbot Starter Template

Una plantilla base completa para desarrollar aplicaciones web interactivas con Streamlit y APIs de IA. Este template proporciona una estructura sólida y funcional que puedes usar como punto de partida para cualquier aplicación de Streamlit que requiera integración con modelos de lenguaje.

## Características

* **Estructura modular** - Código organizado y fácil de mantener
* **Integración con APIs de IA** - Configurado para Together AI (fácilmente adaptable a otras APIs)
* **Gestión de estado** - Implementación correcta del session_state de Streamlit
* **Chat interactivo** - Interfaz de chat completa con historial de mensajes
* **Configuración flexible** - Soporte para variables de entorno y configuración directa
* **Manejo de errores** - Sistema robusto de manejo de respuestas y errores
* **Responsive design** - Interfaz adaptable a diferentes dispositivos
* **Fácil personalización** - Estructura clara para modificar según tus necesidades

## Requisitos

* **Python 3.8 o superior**
* **Cuenta de API** (Together AI u otra según tu elección)
* **Conexión a internet** (para comunicación con APIs)

## Instalación

Sigue estos pasos para configurar tu entorno de desarrollo:

1. **Clona el repositorio:**
```bash
git clone https://github.com/juxnbernxrdo/streamlit-ai-template.git
cd streamlit-ai-template
```

2. **Crea un entorno virtual (recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instala las dependencias necesarias:**
```bash
pip install streamlit together python-dotenv
```

## Configuración de API

Para utilizar este template, necesitas configurar tu clave API:

### 1. Obtener la clave API

1. Visita el proveedor de API de tu elección (ejemplo: [Together AI](https://www.together.ai/))
2. Crea una cuenta o inicia sesión
3. Navega a la sección de API Keys
4. Genera una nueva clave API

### 2. Configurar la clave API

Tienes dos opciones para configurar tu clave API:

**Opción A: Variable de entorno (recomendado para seguridad)**

Crea un archivo `.env` en el directorio raíz del proyecto:

```bash
touch .env
```

Añade tu clave API al archivo `.env`:

```env
TOGETHER_API_KEY=tu_clave_api_aqui
```

**Opción B: Directamente en el código**

Modifica la línea correspondiente en tu archivo principal:

```python
api_key = "tu_clave_api_aqui"
```

**⚠️ Importante:** Si usas la Opción B, nunca compartas tu código con la clave API incluida ni lo subas a repositorios públicos.

## Uso

Una vez completada la configuración, ejecuta tu aplicación:

```bash
streamlit run main.py
```

La aplicación se abrirá en tu navegador en `http://localhost:8501`.

### Comandos útiles para desarrollo:

```bash
# Ejecutar en un puerto específico
streamlit run main.py --server.port 8080

# Ejecutar con recarga automática (útil para desarrollo)
streamlit run main.py --server.runOnSave true

# Ejecutar sin abrir el navegador automáticamente
streamlit run main.py --server.headless true
```

## Estructura del Proyecto

```
streamlit-ai-template/
│
├── main.py               # Aplicación principal de Streamlit
├── .env                  # Variables de entorno (no incluir en git)
├── .gitignore           # Archivos a ignorar por Git
├── README.md            # Este archivo
├── requirements.txt     # Dependencias del proyecto (opcional)
└── components/          # Componentes personalizados (opcional)
    └── __init__.py
```

### Dependencias principales:

- `streamlit` - Framework para aplicaciones web de datos
- `together` - Cliente para APIs de IA (puede cambiarse por otras librerías)
- `python-dotenv` - Manejo de variables de entorno (opcional)

## Personalización

### Modificar el System Prompt

Edita la variable `system_prompt` en el archivo principal para cambiar el comportamiento de tu IA:

```python
system_prompt = """
Tu prompt personalizado aquí...
"""
```

### Cambiar el modelo de IA

Modifica el modelo en la función de respuesta:

```python
response = client.chat.completions.create(
    model="tu-modelo-preferido",  # Cambia aquí
    messages=messages,
    max_tokens=500,
    temperature=0.7,
)
```

### Personalizar la interfaz

Modifica los elementos de Streamlit según tus necesidades:

```python
st.title("Tu Título Personalizado")
st.write("Tu descripción personalizada")
```

## Ejemplos de Uso

Este template es ideal para desarrollar:

- **Chatbots especializados** - Asesores, tutores, consultores virtuales
- **Herramientas de análisis** - Análisis de texto, datos, documentos
- **Asistentes creativos** - Generación de contenido, brainstorming
- **Aplicaciones educativas** - Tutores personalizados, explicadores
- **Herramientas empresariales** - Análisis de mercado, estrategia, reportes

## Buenas Prácticas

### Seguridad
- Nunca hardcodees claves API en el código
- Usa variables de entorno para información sensible
- Añade `.env` a tu `.gitignore`

### Performance
- Usa `@st.cache_data` para funciones que procesan datos
- Implementa loading spinners para operaciones lentas
- Considera pagination para grandes volúmenes de datos

### UX/UI
- Proporciona feedback visual durante procesamientos
- Maneja errores graciosamente
- Usa session_state apropiadamente para mantener estado

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Créditos

Este template ha sido desarrollado utilizando las siguientes tecnologías:

* **[Python](https://www.python.org/)** - Lenguaje de programación principal
* **[Streamlit](https://streamlit.io/)** - Framework para aplicaciones web de datos
* **[Together AI](https://www.together.ai/)** - Ejemplo de proveedor de API de IA
* **[OpenAI](https://openai.com/)** - Inspiración en interfaces conversacionales

---

**¿Tienes preguntas o problemas?** Abre un [issue](https://github.com/juxnbernxrdo/streamlit-ai-template/issues) en GitHub para obtener ayuda.

⭐ **¡Si este template te es útil, no olvides darle una estrella en GitHub!**

🚀 **¡Empieza a desarrollar aplicaciones increíbles con Streamlit!**
