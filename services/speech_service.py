from gtts import gTTS

def text_to_speech(text:str):
    file_name="speech.mp3"
    tts=gTTS(text=text, lang="en")
    tts.save(file_name)
    return file_name