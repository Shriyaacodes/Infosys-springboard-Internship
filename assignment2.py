import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyttsx3
import time

# Set the duration of the audio recording (in seconds)
duration = 5  # for a 5-second audio recording

# Set the sample rate (standard is 44100)
sample_rate = 44100

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to record audio using sounddevice
def record_audio(duration, sample_rate):
    print("Preparing to record...")
    time.sleep(1)  # Short delay to prepare the microphone
    print("Recording...")
    sd.stop()  # Clear any previous buffer
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    print("Recording complete.")
    return audio_data

# Function to recognize speech from the recorded audio
def recognize_speech(audio_data, sample_rate):
    # Create a new recognizer instance each time
    recognizer = sr.Recognizer()
    
    # Convert numpy array to AudioData
    audio_data = np.array(audio_data, dtype=np.int16)
    audio_data = sr.AudioData(audio_data.tobytes(), sample_rate, 2)
    
    # Try to recognize the speech using Google's speech recognition
    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio_data)
        print(f"Recognized Text: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results from the speech recognition service.")
        return None

# Function to generate responses based on the recognized text
def generate_response(text):
    if "hello" in text.lower() or "hi" in text.lower():
        return "Hello! How can I assist you?"
    elif "how are you" in text.lower():
        return "I'm fine, thank you! How about you?"
    elif "your name" in text.lower():
        return "I am your voice assistant."
    elif "what is the weather" in text.lower():
        return "Sorry, I don't have access to weather data right now."
    elif "exit" in text.lower() or "quit" in text.lower():
        return "Goodbye!"
    else:
        return "I'm not sure how to respond to that."

# Function to speak the recognized or generated text
def speak_text(text):
    if text:
        print(f"Assistant: {text}")
        engine.say(text)  # Convert text to speech
        engine.runAndWait()  # Play the speech out loud

# Main loop to record and process multiple times
while True:
    # Record audio
    audio_data = record_audio(duration, sample_rate)

    # Recognize and display the speech
    recognized_text = recognize_speech(audio_data, sample_rate)

    # If text is recognized, generate a response and speak it
    if recognized_text:
        response = generate_response(recognized_text)
        speak_text(response)
        
        # Exit if the user says "exit" or "quit"
        if "exit" in recognized_text.lower() or "quit" in recognized_text.lower():
            print("Exiting the program.")
            break
    else:
        print("No valid speech recognized.")
