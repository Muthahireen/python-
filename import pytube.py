import pytube
 
link = input('Enter YouTube video link')
yt = pytube.YouTube(link)
yt.streams.first().download()
print('downloaded',link)