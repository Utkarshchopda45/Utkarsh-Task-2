#Internship Task 2

#  first install pytube on cmd
# package import
from pytube import YouTube

# link for youtube video in ''
url = 'https://youtu.be/sFw8GRyur0M'
youtube_name = YouTube(url)

# tital for youtube
print(youtube_name.title)

print("###Video Title###")

#thumbnail for youtube
print(youtube_name.thumbnail_url)

print("###video Tumbnail###")

#downlod the video
print("###downlod video###")

# resolutation stream
youtube_name = youtube_name.streams.get_highest_resolution()

youtube_name.download()