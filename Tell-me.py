# task3.py - Tell Me App with Streamlit GUI
import streamlit as st
import pyttsx3
import pdfplumber
from pathlib import Path

# ------------------------
# PDF Reader Function
# ------------------------
def read_pdf(file_path):
    text_content = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:  # check if page has text
                text_content += text + "\n"
    return text_content


# ------------------------
# Text to Speech Function
# ------------------------
def text_to_speech(text, voice, rate):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    
    # Set voice (male/female)
    if voice == "Female" and len(voices) > 1:
        engine.setProperty("voice", voices[1].id)
    else:
        engine.setProperty("voice", voices[0].id)

    # Set speaking rate
    engine.setProperty("rate", rate)

    # Save to file
    output_path = Path("output_audio.mp3")
    engine.save_to_file(text, str(output_path))
    engine.runAndWait()
    return output_path


# ------------------------
# Streamlit App UI
# ------------------------
def main():
    st.set_page_config(page_title="Tell Me", page_icon="📖")
    st.title("📖 Tell Me - Text to Speech App")

    st.markdown("This app can read your **text or PDF** aloud with adjustable voice and speed.")

    # Sidebar for settings
    st.sidebar.header("⚙️ Settings")
    voice = st.sidebar.radio("Choose Voice", ["Male", "Female"])
    rate = st.sidebar.slider("Speech Speed (words per minute)", 100, 200, 150)

    # Input Section
    st.subheader("✍️ Enter Text or Upload PDF")
    text = st.text_area("Enter your text here:")

    uploaded_file = st.file_uploader("Or upload a PDF file", type=["pdf"])
    if uploaded_file is not None:
        text = read_pdf(uploaded_file)
        st.success("✅ PDF loaded successfully!")

    # Action button (only one instance now)
    if st.button("🎤 Read Aloud"):
        if text.strip():
            st.info("🔊 Generating speech, please wait...")
            audio_file = text_to_speech(text, voice, rate)
            st.audio(str(audio_file))
            with open(audio_file, "rb") as f:
                st.download_button("⬇️ Download Audio", f, file_name="tellme_audio.mp3")
        else:
            st.warning("⚠️ Please enter text or upload a PDF first.")


if __name__ == "__main__":
    main()
