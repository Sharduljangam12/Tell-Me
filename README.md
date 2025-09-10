📖 Tell Me - Text to Speech App

A simple yet powerful Streamlit-based application that converts text or PDF files into speech.
Built with Streamlit, pyttsx3, and pdfplumber, this app provides offline text-to-speech conversion with customizable voice (Male/Female) and speed settings.

🚀 Features

🎤 Text-to-Speech (TTS): Converts typed text or PDF content into speech.

📂 PDF Support: Upload a .pdf file, and the app will read it aloud.

🗣 Voice Options: Choose between Male and Female voices.

⚡ Adjustable Speed: Control speech rate (100–200 words per minute).

💾 Downloadable Audio: Save generated speech as tellme_audio.mp3.

🖥 Web-based GUI: Clean and interactive UI powered by Streamlit.

📴 Offline Support: Works without an internet connection using pyttsx3.

🛠️ Tech Stack

Frontend / GUI: Streamlit

Text-to-Speech Engine: pyttsx3
 (offline TTS library)

PDF Parsing: pdfplumber

File Handling: Python pathlib

▶️ Usage

Run the Streamlit app:

streamlit run task3.py


Enter text manually OR upload a PDF file.

Choose voice (Male / Female) and set speech speed.

Click 🎤 Read Aloud to generate speech.

Listen in-app OR download the generated .mp3 file.

Project Structure 
📦 tell-me-app
 ┣ 📜 task3.py          # Main application code
 ┣ 📜 requirements.txt  # Dependencies
 ┣ 📜 README.md         # Documentation
 ┗ 📂 output            # Generated audio files (optional)
