import streamlit as st
import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

st.title("Speech Recognition Kiosk for Order Taking")
st.write("Click the button below to start speaking your order.")

# Button to activate speech recognition
if st.button("Start Recording"):
    with sr.Microphone() as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        
        st.write("Processing...")
        try:
            # Recognize speech using Google's free speech-to-text service
            text = recognizer.recognize_google(audio)
            st.write("You said:", text)
            
        except sr.UnknownValueError:
            st.write("Sorry, I could not understand the audio.")
        except sr.RequestError:
            st.write("Could not request results from the speech service.")

st.write("Designed to assist with hands-free order taking.")
