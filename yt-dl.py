from pytube import YouTube

"""
    accept the input from the user and pass on the link to the
    YouTube class. It will help us reveal all the information about the
    video and also will let us download it.
"""
link = input("Enter the link: ")
yt = YouTube(link)

# Revealing various information about the video

# Title of video
print("Title : ", yt.title)

# Number of views of video
"""
    using the format() function to add a comma to
    every thousand place starting from the left
"""
views = "{:,}".format(yt.views)
print("Number of views : ", views)

# Length of the video
print("Length of video : ", yt.length, " seconds")

# create store the highest resolution stream in the ys variable.
yt_video = yt.streams.get_highest_resolution()

print("Downloading...")
# we have stored our perferred stream in a variable ys. Now, we download it
# to our system
yt_video.download('~/Downloads')

print("Download completed!")
