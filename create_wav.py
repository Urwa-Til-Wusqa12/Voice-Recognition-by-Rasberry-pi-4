from gtts import gTTS
import os

# Text to convert
text = "Hello, I am a Raspberry Pi speaking"

# Create mp3
tts = gTTS(text)
tts.save("output.mp3")

# Convert to WAV (Mono, 16kHz)
os.system("ffmpeg -i output.mp3 -ar 16000 -ac 1 output.wav")
