import whisper
model = whisper.load_model("base")
transcription = model.transcribe(r"audio.mp3")
print(transcription["text"])

