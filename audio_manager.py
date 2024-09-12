'''
packages

pip install gtts pygame
pip install SpeechRecognition

'''
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from gtts import gTTS
import io
import speech_recognition as sr
import threading


class AudioManager:
    def __init__(self, max_time=10):
        self.max_time = max_time

    def listen(self):
        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Use the microphone as the audio source
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Reduce noise
            print("Listening...")
            audio = recognizer.listen(source)  # Capture the audio

            try:
                print("Recognizing...")
                # Use Google Web Speech API to recognize the speech
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError:
                print("Sorry, the service is unavailable.")

        return None

    def record(self, file_name="my_recording.wav"):
        pass

    def speak(self, text):
        tts = gTTS(text=text, lang='en')
        # Save the speech to a file-like object in memory (BytesIO)
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        self.play(audio_fp)

    def play(self, audio_file):
        # Initialize the mixer
        pygame.mixer.init()

        # Load the audio file
        pygame.mixer.music.load(audio_file)

        # Play the audio
        pygame.mixer.music.play()

        # Wait until the music finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(self.max_time)

    def speak_async(self, text):
        # Run the speak method in a separate thread
        threading.Thread(target=self.speak, args=(text,), daemon=True).start()

if __name__ == "__main__":
    audio_manager = AudioManager()
    # audio_manager.speak("Hello, I am converting text to voice using Python and playing it directly!")
    # audio_manager.play("output.mp3")
    # audio_manager.record()
    audio_manager.listen()