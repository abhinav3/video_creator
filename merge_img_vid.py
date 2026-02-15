# !pip install moviepy==1.0.3 
from moviepy import ImageClip, AudioFileClip

# Load assets
audio = AudioFileClip("/Users/aravi2/Downloads/sambhu.mp3")
clip = ImageClip("/Users/aravi2/Downloads/shiv_barati.png", duration=audio.duration)

# Set audio and write file with AAC codec
clip = clip.with_audio(audio)
clip.write_videofile("/Users/aravi2/Downloads/video.mp4", fps=24, audio_codec="aac") # <-- Added audio_codec
