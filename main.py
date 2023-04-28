#Importing the libraries
from fastapi import FastAPI
from bark import SAMPLE_RATE, generate_audio
from scipy.io.wavfile import write as write_wav

#Creating the app object
app = FastAPI()

#Defining the home page of the API
@app.get("/")
async def root():
    return {"message": "Welcome to the API of Bark!"}

#Defining the generate audio endpoint
@app.post("/generate-audio")
async def generate_audio_endpoint(prompt: str):
    audio_array = generate_audio(prompt)
    write_wav("/app/audio.wav", SAMPLE_RATE, audio_array)
    return {"file": "/app/audio.wav", "rate": SAMPLE_RATE}
