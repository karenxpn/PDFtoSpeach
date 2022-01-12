from google.cloud import texttospeech
from pdfminer.high_level import extract_text
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/karenmirakyan/Downloads/pdftospeach-0d1a23eedcd7.json"

output = extract_text('sample_pdf_file.pdf')

client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(text=output)
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
