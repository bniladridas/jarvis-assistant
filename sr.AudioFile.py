import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def process_audio_file(file_path):
    """
    Process the given audio file, convert speech to text, 
    generate a response, and play the response as audio.
    """
    recognizer = sr.Recognizer()

    try:
        print("Processing audio file...")
        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)
            print("Audio recorded successfully.")

        # Recognize speech using Google Web Speech API
        try:
            text = recognizer.recognize_google(audio_data)
            print(f"You just expressed: {text}")
        except sr.UnknownValueError:
            text = "Sorry, I could not understand the audio."
            print("Speech recognition could not understand the audio.")
        except sr.RequestError as e:
            text = "Speech recognition is currently unavailable."
            print(f"Error with the speech recognition service: {e}")

        # Generate a response
        response_text = generate_response(text)
        print(f"Response: {response_text}")

        # Convert the response text to speech and play it
        text_to_speech(response_text)

    except FileNotFoundError:
        print("Audio file not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def generate_response(user_input):
    """
    Generate a response based on user input.
    This function can be customized further.
    """
    if "hello" in user_input.lower():
        return "Hi there! How can I assist you today?"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    elif "thanks" in user_input.lower():
        return "You're welcome!"
    else:
        return "I'm here to help! How can I assist you today?"

def text_to_speech(response_text):
    """
    Convert the response text to speech and play it using pydub.
    """
    try:
        # Generate speech from text
        tts = gTTS(response_text, lang='en')
        output_file = "output.mp3"
        tts.save(output_file)
        print("Text-to-speech conversion successful. Playing the response...")

        # Play the audio file
        audio = AudioSegment.from_file(output_file, format="mp3")
        play(audio)

    except Exception as e:
        print(f"Error during text-to-speech playback: {e}")

# Main execution block
if __name__ == "__main__":
    try:
        # Replace with the actual path to your audio file
        audio_file_path = "/workspaces/voice-assistant-chatbot/test.wav"
        process_audio_file(audio_file_path)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")