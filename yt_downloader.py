from pytube import Youtube

url = input('Enter URL :')

# yt object
yt = Youtube(url)

print('Title :',yt.title)
print('')