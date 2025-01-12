
# installing required packages
# pip install pytube OR
# python -m pip install git+https://github.com/pytube/pytube   

# importing required packages
from pytube import YouTube

# taking URL from user
url = input("Enter the YouTube URL: ")

# main logic
try:
    yt = YouTube(url)
    # Get a progressive stream (contains both audio and video)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download()
    print("Download completed successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
