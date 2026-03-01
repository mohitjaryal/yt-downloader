from pytube import YouTube

url = input('Enter URL :')

# yt object
yt = YouTube(url)

print('Title :',yt.title)
print('Availabe Streams :')
for stream in yt.streams.filter(progressive=True):
    print(stream)


stream = yt.stream.get_highest_resolution()
print('Downloading :', yt.title)
stream.download()
print('Dodnload Complete:')