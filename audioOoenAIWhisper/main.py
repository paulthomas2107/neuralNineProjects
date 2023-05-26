import whisper

model = whisper.load_model("base")
result = model.transribe("harvard.wav")
