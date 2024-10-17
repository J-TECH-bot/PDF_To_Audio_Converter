import PyPDF2
from gtts import gTTS
import os

def pdf_to_audio(pdf_path, audio_path):
    # Open the PDF file in read-binary mode
    pdf_file = open(pdf_path, 'rb')
    
    # Create a PyPDF2 reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Initialize an empty string to hold the text
    text = ''
    
    # Iterate through all the pages and extract text from each page
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()
    
    # Close the PDF file
    pdf_file.close()
    
    # Check if text is not empty before proceeding
    if text:
        # Print the text to verify its content
        print("Extracted Text:", text[:100], "...")  # Show the first 100 characters
        
        # Proceed with converting text to speech
        tts = gTTS(text=text, lang='en')
        tts.save(audio_path)
        print("Audio saved successfully.")
    else:
        print("No text extracted from the PDF.")

# Example usage
pdf_path = 'C://Users//acer//Documents//PdftoAudio//file1.pdf'
audio_path = 'C://Users/acer//Documents//PdftoAudio//audio/audio.mp3'
pdf_to_audio(pdf_path, audio_path)
