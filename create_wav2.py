from gtts import gTTS
import os

# Text to convert
text = "Hi. I am Urwa. I am currently doing a project on the easpberry pi . the project is about a speech reconition system."

# Create mp3
tts = gTTS(text)
tts.save("test2.mp3")

# Convert to WAV (Mono, 16kHz)
os.system("ffmpeg -i test2.mp3 -ar 16000 -ac 1 test2.wav")
