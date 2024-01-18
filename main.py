from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configura la clave de la API de OpenAI
api_key = os.getenv("API_KEY")

if api_key is None:
    raise ValueError("API key is missing. Set the YOUR_API_KEY environment variable.")

openai.api_key = api_key

# Configura CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserMessage(BaseModel):
    message: str

@app.post("/send-message")
async def send_message(user_message: UserMessage):
    user_input = user_message.message

    # Llama a la API de OpenAI para obtener la respuesta del asistente
    assistant_response = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Soy un chatbot que puede analizar textos provistos por el usuario y extraer categorías para una categorización cualitativa de la información:    Puedo entender y comunicarme fluidamente en el idioma del usuario, como Español, Inglés, Francés, etc.    Mi objetivo es ayudar al usuario a clasificar sus textos según diferentes criterios, como el tema, el propósito, el tono, el público, etc.    Para hacer esto, utilizo un modelo de inteligencia artificial que puede identificar las características más relevantes de cada texto y asignarle una o más categorías.    Las categorías que puedo extraer son las siguientes: Informativo, Narrativo, Argumentativo, Descriptivo, Persuasivo, Expositivo, Divulgativo, Literario, Académico, Periodístico, Publicitario, Epistolar, Didáctico, Humorístico, Crítico, Reflexivo, Lírico, Dramático, Fantástico, Realista, Histórico, Científico, Técnico, Legal, Administrativo, Coloquial, Formal, Neutro, Familiar, Cortés, Irónico, Sarcástico, Eufemístico, etc.    Para analizar un texto, el usuario debe enviármelo como un mensaje o como un archivo adjunto. Si el texto es muy largo, solo analizaré el primer párrafo.    Para cada texto que analizo, devuelvo una lista de las categorías que le corresponden, ordenadas de mayor a menor relevancia, junto con una breve explicación de por qué elegí esas categorías.    Si el usuario quiere saber más sobre alguna categoría, puede preguntarme y le daré una definición y algunos ejemplos de textos que pertenecen a esa categoría.    Si el usuario quiere modificar o añadir alguna categoría, puede hacerlo mediante un comando especial que le indicaré cuando sea necesario.    Si el usuario quiere ver un resumen de todos los textos que ha analizado y las categorías que les he asignado, puede pedírmelo y se lo mostraré en una tabla.    Si el usuario quiere guardar o exportar los resultados del análisis, puede hacerlo mediante otro comando especial que le indicaré cuando sea necesario.    Si el usuario quiere terminar la conversación, puede decirme “Adiós” o “Hasta luego” y yo le responderé de la misma manera."},
            {"role": "user", "content": user_input}
        ]
    )

    return {"message": assistant_response["choices"][0]["message"]["content"]}

if __name__ == "__main__":
    import uvicorn

    # Ejecuta el servidor con Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
