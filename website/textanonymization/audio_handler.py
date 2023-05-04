import speech_recognition as sr


def get_text_from_audio(audio_file: str):
    r = sr.Recognizer()

    # Open the audio file using the recognizer
    with sr.AudioFile(audio_file) as source:
        # Record the audio from the file
        audio_text = r.record(source)

    # Use the recognizer to recognize the speech in the audio
    try:
        text = r.recognize_google(audio_text)
        return text
    except sr.UnknownValueError:
        print('Speech recognition could not understand audio')
    except sr.RequestError as e:
        print('Error: ', e)
