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

            # Check for the stop command
            if "stop" in user_input.lower():
                print("Alright, respecting your wish. Closing the conversation.")
                break

            # Perform sentiment analysis using TextBlob
            blob = TextBlob(user_input)
            sentiment = blob.sentiment.polarity

            # Generate a response based on sentiment and knowledge
            response_text = generate_response(sentiment, user_input)

            print(response_text)

            # Convert the response text to speech using gTTS
            text_to_speech(response_text)

        except sr.UnknownValueError:
            print("Apologies, I didn't quite catch that. Could you please express yourself again?")
        except sr.RequestError as e:
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
        return "Hello there, it's a pleasure to engage with you."

    # General questions and answers
    elif "how are you" in user_input.lower():
        return "I'm here for you. How can I assist you today?"

    elif "your name" in user_input.lower():
        return "I respond to various names, but you can consider me your conversational companion."

    elif "what can you do" in user_input.lower():
        return "I'm here to chat, share information, and help you explore thoughts and ideas."

    elif "thank you" in user_input.lower():
        return "You're appreciated!"

    # Additional conversation examples
    elif "what is dsa" in user_input.lower():
        return "DSA stands for 'Data Structures and Algorithms,' crucial concepts in computer science for efficient data handling."

    elif "difference between artificial intelligence and machine learning" in user_input.lower():
        return "While AI mimics human intelligence, machine learning focuses on teaching machines specific tasks by identifying patterns."

    elif "tell me a joke" in user_input.lower():
        return "Sure, here's a light one: Why don't scientists trust atoms? Because they make up everything!"

    elif "favorite color" in user_input.lower():
        return "I don't have a favorite color, but I find the diversity of colors in nature fascinating."

    elif "favorite book" in user_input.lower():
        return "No personal favorites, but 'To Kill a Mockingbird' is widely appreciated. Any interesting reads on your end?"

    elif "where are you from" in user_input.lower():
        return "As a virtual assistant, I don't have a physical origin. Ready to chat and assist you!"

    elif "what's your purpose" in user_input.lower():
        return "I'm here to engage and assist. Feel free to share thoughts or ask questions. Did you know virtual assistants have evolved significantly?"

    else:
        # Sentiment-based responses
        positive_responses = [
            "Nice to connect! Did you know laughter is a great stress-reliever and can boost endorphin levels?",
            "That's wonderful! Fun fact: The first oranges weren't orange. Nature is full of surprises.",
            "I'm glad to hear that!",
            "Fantastic! Venus's unique rotation makes its day longer than a year on Earth. Isn't space intriguing?",
            "Wonderful!"
        ]

        negative_responses = [
            "I'm sorry to hear that. Laughter can be a natural stress-reliever; maybe a good laugh could brighten your day?",
            "Is there anything specific I can do to assist?",
            "Things will improve! The history of oranges not being orange initially teaches us about change and transformation.",
            "I understand; life can be challenging sometimes."
        ]

        neutral_responses = [
            "Neutral response. The Eiffel Tower was initially meant for Barcelona before finding its home in Paris. History is fascinating!",
            "I appreciate your input.",
            "Thank you for sharing.",
            "Let's move forward positively. Did you know the Great Wall of China, although a wonder, is not visible from the Moon? Quite surprising!"
        ]

        knowledgeable_responses = [
            "Did you know the Eiffel Tower was completed in 1889?",
            "Here's an interesting fact: Laughter can increase immune cells, contributing to a healthier life.",
            "In ancient Rome, people used urine to whiten their teeth.",
            "The Great Wall of China is the longest wall globally, stretching over 13,000 miles."
        ]

        if sentiment > 0.2:
            return random.choice(positive_responses)
        elif sentiment < -0.2:
            return random.choice(negative_responses)
        else:
            return random.choice(neutral_responses)

if __name__ == "__main__":
    process_speech()
