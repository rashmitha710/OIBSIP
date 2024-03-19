# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:30:28 2024

@author: Rashmitha
"""

import speech_recognition as sr
import pyttsx3

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")
            return ""
        except sr.RequestError:
            print("Sorry, there was an error recognizing your voice.")
            return ""

# Main function
def main():
    speak("Hello! I'm your voice assistant. How can I help you?")
    while True:
        command = listen()
        if "hello" in command:
            speak("Hi there!")
        elif "what's your name" in command:
            speak("I'm a voice assistant.")
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I'm not programmed to do that yet.")

# Check if the script is being run directly
if __name__ == "__main__":
    main()