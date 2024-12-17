import speech_recognition as sr
from textblob import TextBlob
from gtts import gTTS
from playsound import playsound
import random

def process_speech():
    # Initialize the speech recognizer
    recognizer = sr.Recognizer()

    while True:
        # Capture audio from the microphone
        with sr.Microphone() as source:
            print("Go ahead, share your thoughts:")
            audio = recognizer.listen(source)

        try:
            # Convert speech to text using Google's Web Speech API
            user_input = recognizer.recognize_google(audio)
            print(f"You just expressed: {user_input}")

            # Check for the stop command to end the conversation
            if "stop" in user_input.lower():
                print("Alright, respecting your wish. Closing the conversation.")
                break

            # Perform sentiment analysis using TextBlob
            blob = TextBlob(user_input)
            sentiment = blob.sentiment.polarity

            # Generate a response based on sentiment and user input
            response_text = generate_response(sentiment, user_input)

            print(response_text)

            # Convert the response text to speech using gTTS
            text_to_speech(response_text)

        except sr.UnknownValueerror:
            # Handle case where speech was not understood
            print("Apologies, I didn't quite catch that. Could you please express yourself again?")
        except sr.RequestError as e:
            # handle case where there was an error with the Google API request
            print(f"Oops! There was an error connecting to the Google API: {e}")

def text_to_speech(text):
    # Use gTTS to convert text to speech and save it as an MP3 file
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")

    # Play the generated audio file using playsound
    playsound("output.mp3")

def generate_response(sentiment, user_input):
    # Acknowledge user's introduction and provide relevant information
    if "hi" in user_input.lower() and "miya" in user_input.lower():
        return "Hello there, it's a pleasure to engage with you, Miya."

    # General questions and answers
    elif "how are you" in user_input.lower():
        return "I'm here and ready to assist you. How can I help you today?"

    elif "your name" in user_input.lower():
        return "I respond to various names, but you can consider me your conversational companion."

    elif "what can you do" in user_input.lower():
        return "I can chat, share information, and assist you with various tasks. What would you like to know more about?"

    elif "thank you" in user_input.lower():
        return "You're welcome! If you need anything else, feel free to ask."

    # Additional conversation examples
    elif "what is dsa" in user_input.lower():
        return "DSA stands for 'Data Structures and Algorithms,' which are fundamental concepts in computer science for efficient data handling."

    elif "difference between artificial intelligence and machine learning" in user_input.lower():
        return "Artificial Intelligence (AI) is the broader concept of machines performing tasks that require human-like intelligence. Machine Learning (ML) is a subset of AI that focuses on teaching machines to learn from data and improve over time."

    elif "tell me a joke" in user_input.lower():
        return "Sure, here's a light one: Why don't scientists trust atoms? Because they make up everything!"

    elif "favorite color" in user_input.lower():
        return "I don't have a favorite color, but I find the diversity of colors in nature fascinating. What's your favorite color?"

    elif "favorite book" in user_input.lower():
        return "I don't have a favorite book, but 'To Kill a Mockingbird' is widely appreciated. Any interesting reads on your end?"

    elif "where are you from" in user_input.lower():
        return "As a virtual assistant, I don't have a physical origin. I exist to chat and assist you. How can I help you today?"

    elif "what's your purpose" in user_input.lower():
        return "My purpose is to engage and assist you. Feel free to share thoughts or ask questions. Did you know virtual assistants have evolved significantly over the years?"

    else:
        # Sentiment-based responses
        positive_responses = [
            "That's great to hear! Did you know that laughter can boost endorphin levels and reduce stress?",
            "Wonderful! Fun fact: The first oranges weren't actually orange. Nature is full of surprises.",
            "I'm glad to hear that! Did you know that Venus has a longer day than a year due to its unique rotation?",
            "Fantastic! What's the best part of your day so far?",
            "That's wonderful! What's on your mind today?"
        ]

        negative_responses = [
            "I'm sorry to hear that. Laughter can be a natural stress-reliever; maybe a good laugh could brighten your day?",
            "Is there anything specific I can do to assist you?",
            "Things will improve! Did you know that the first oranges weren't actually orange? Change and transformation can be fascinating.",
            "I understand; life can be challenging sometimes. What's been the highlight of your day?"
        ]

        neutral_responses = [
            "Neutral response. The Eiffel Tower was initially meant for Barcelona before finding its home in Paris. History is fascinating!",
            "I appreciate your input. How can I assist you further?",
            "Thank you for sharing. What would you like to discuss next?",
            "Let's move forward positively. Did you know the Great Wall of China is the longest wall globally, stretching over 13,000 miles?"
        ]

        knowledgeable_responses = [
            "Did you know the Eiffel Tower was completed in 1889?",
            "Here's an interesting fact: Laughter can increase immune cells, contributing to a healthier life.",
            "In ancient Rome, people used urine to whiten their teeth.",
            "The Great Wall of China is the longest wall globally, stretching over 13,000 miles."
        ]

        # Choose a response based on the sentiment polarity
        if sentiment > 0.2:
            return random.choice(positive_responses)
        elif sentiment < -0.2:
            return random.choice(negative_responses)
        else:
            return random.choice(neutral_responses)

if __name__ == "__main__":
    process_speech()