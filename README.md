# Voice-Recognition-by-Rasberry-pi-4

A simple speech recognition project implemented on Raspberry Pi using Python. This project demonstrates converting text to speech using gTTS, then recognizing the generated speech using the SpeechRecognition library.


**🔧 Tools & Technologies Used:**

1:Raspberry Pi OS (32-bit)

2:Python 3.11

3:gTTS (Google Text-to-Speech)

4:SpeechRecognition

5:ffmpeg (for converting MP3 to WAV)

6:Thonny IDE

7:Raspberry Pi terminal / CLI

**📁 Project Files Overview:**

File Description:

   1:create_wav.py: Converts custom text to speech and generates output.wav from output.mp3.(instead of creating you can use a downloaded wav file also.)
   
   2:create_wav2.py: Similar to above, generates test2.wav from test2.mp3.
   
   3:task2raspberrypi.py: Performs speech-to-text conversion on a given .wav file using the speech_recognition module.
   

**⚙️ Setup Instructions:**

**1:Install Required Packages:**

pip install gTTS SpeechRecognition

sudo apt-get install ffmpeg

**2:Create a Virtual Environment**

python3 -m venv env

source env/bin/activate

**3:Generate Audio Files:**

python create_wav.py

python create_wav2.py

-> This will create:

output.mp3 → converted to output.wav

test2.mp3 → converted to test2.wav

**4:Run Speech Recognition:**
python task2raspberrypi.py output.wav

python task2raspberrypi.py test2.wav

✅ **The output in both cases accurately reflects the spoken text.**

✅ **Significance of project:**

i):Rather than using pre-existing .wav files, text-to-speech is dynamically generated with gTTS.

ii):Demonstrates a full pipeline from TTS to STT on a Raspberry Pi.

iii):Clean separation of modules for better readability and reuse.
