![SpeechRecognition](https://img.shields.io/badge/-SpeechRecognition-009688?style=flat-square&logo=python&logoColor=white)
![TextBlob](https://img.shields.io/badge/-TextBlob-009688?style=flat-square&logo=python&logoColor=white)
![gTTS](https://img.shields.io/badge/-gTTS-009688?style=flat-square&logo=python&logoColor=white)
![playsound](https://img.shields.io/badge/-playsound-009688?style=flat-square&logo=python&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)

[![Watch the video](/data/Screenshot.png)](https://youtube.com/shorts/o_ZbD5GS5VY?si=gU2_Tp94G5UwC0DV)



# Voice Assistant Chatbot

This repository contains a simple voice assistant chatbot built using Python. The chatbot is capable of understanding user speech, processing it, and generating a spoken response. It utilizes various libraries, including SpeechRecognition, TextBlob, gTTS, and playsound, to handle speech recognition, sentiment analysis, text-to-speech conversion, and audio playback, respectively.

## Getting Started

To run the voice assistant chatbot, follow these steps:

1. **Prerequisites**
   Make sure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

2. **Install Required Libraries**
   You need to install the following libraries if you haven't already:
   - SpeechRecognition
   - TextBlob
   - gTTS
   - playsound
   Install them using pip:

3. **Run the Chatbot**
Run the `nlp.py` script to start the voice assistant chatbot:

4. **Interact with the Chatbot**
Speak to the chatbot, and it will respond based on the input provided. To stop the chatbot, say "stop".

## Functionality

The voice assistant chatbot offers the following functionality:

- Speech recognition: Capturing audio from the microphone and converting it to text using Google's Web Speech API
- Sentiment analysis: Analyzing the sentiment of the user input using TextBlob
- Text-to-speech conversion: Converting the response text to speech using gTTS
- Diverse responses: Generating various responses based on user input, sentiment, and knowledge

## File Structure

- `nlp.py`: The main script that runs the chatbot

## Contributing

Contributions are welcome! If you have any suggestions or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/niladrridas/voice-assistant-chatbot/blob/main/LICENSE) file for details.

## Acknowledgements

- [SpeechRecognition](https://github.com/Uberi/speech_recognition): A Python library for performing speech recognition, with support for various engines and APIs.
- [TextBlob](https://github.com/sloria/TextBlob): A Python library for processing textual data.
- [gTTS](https://github.com/pndurette/gTTS): A Python library and CLI tool to interface with Google's Text-to-Speech API.
- [playsound](https://github.com/TaylorSMarks/playsound): A simple Python module for playing sounds using the `winsound` module on Windows and the `afplay` or `aplay` command on macOS and Linux.
