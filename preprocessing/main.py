import torch
pipeline = torch.hub.load('pyannote/pyannote-audio', 'dia')
diarization = pipeline("demo.wav")
