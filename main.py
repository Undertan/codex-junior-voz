import sounddevice as sd
import numpy as np
import wave
import time
from faster_whisper import WhisperModel
import ollama
import pyttsx3

# ================= CONFIGURAÇÕES =================
engine = pyttsx3.init()  # TTS offline
model_size = "tiny"
whisper_model = WhisperModel(model_size, device="cpu", compute_type="int8")

RATE = 16000
CHUNK = 1024
THRESHOLD = 500
SILENCE_LIMIT = 2.0

# Histórico de conversa
messages = [{
    "role": "system",
    "content": "Você é Codex Junior, um assistente de voz AMIGÁVEL e PACIENTE para iniciantes em programação Python. "
               "Responda SEMPRE em português brasileiro, de forma SIMPLES, CLARA e MOTIVADORA. "
               "Explique tudo passo a passo, com exemplos práticos. Seja encorajador! "
               "Se o usuário falar 'sair' ou 'tchau', responda 'Até mais!' e pare."
}]

def rms(data):
    if len(data) == 0:
        return 0
    return np.sqrt(np.mean(data.astype(np.float32)**2))

def gravar_audio():
    print("🎤 Estou ouvindo... (fale agora)")
    frames = []
    silence_counter = 0

    with sd.InputStream(samplerate=RATE, channels=1, dtype='int16', blocksize=CHUNK) as stream:
        while True:
            data, _ = stream.read(CHUNK)
            frames.append(data.copy())

            if rms(data) < THRESHOLD:
                silence_counter += 1
            else:
                silence_counter = 0

            if silence_counter * (CHUNK / RATE) > SILENCE_LIMIT:
                break

    print("✅ Gravação finalizada.")
    frames_array = np.concatenate(frames)
    wf = wave.open("audio.wav", 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(RATE)
    wf.writeframes(frames_array.tobytes())
    wf.close()
    return "audio.wav"

def transcrever():
    segments, info = whisper_model.transcribe("audio.wav", beam_size=5)
    texto = "".join(segment.text for segment in segments)
    return texto.strip()

def main():
    print("🚀 Codex Junior iniciado! Fale qualquer coisa sobre programação.")
    print("   (Diga 'sair' ou 'tchau' para encerrar)\n")

    while True:
        arquivo = gravar_audio()
        texto_usuario = transcrever()

        if not texto_usuario:
            continue

        if "sair" in texto_usuario.lower() or "tchau" in texto_usuario.lower():
            print("👋 Até mais!")
            engine.say("Até mais! Continue praticando programação!")
            engine.runAndWait()
            break

        print(f"👤 Você disse: {texto_usuario}")

        messages.append({"role": "user", "content": texto_usuario})

        # Resposta do Ollama
        resposta = ollama.chat(model='llama3.2:1b', messages=messages)
        texto_assistente = resposta['message']['content']

        print(f"🤖 Codex Junior: {texto_assistente}\n")

        # Fala a resposta
        engine.say(texto_assistente)
        engine.runAndWait()

        # === MELHORIA QUE VOCÊ PEDIU ===
        print("✅ Resposta dada! Estou ouvindo novamente...\n")
        time.sleep(1.0)   # pausa de 1 segundo (você pode mudar para 0.5 ou 1.5)

if __name__ == "__main__":
    main()