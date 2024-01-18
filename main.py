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
            {"role": "system", "content": "You are a personal math tutor."},
            {"role": "user", "content": user_input}
        ]
    )

    return {"message": assistant_response["choices"][0]["message"]["content"]}

if __name__ == "__main__":
    import uvicorn

    # Ejecuta el servidor con Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
