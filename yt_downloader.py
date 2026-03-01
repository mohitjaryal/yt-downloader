from pytube import Youtube

url = input('Enter URL :')

# yt object
yt = Youtube(url)

print('Title :',yt.title)
print('Availabe Streams :')
for stream in yt.streams.filter(progressive=True):
    print(stream)

    