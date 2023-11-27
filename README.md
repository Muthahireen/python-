# python-#pip install pytube
import pytube

link = input("Enter YouTube video url:")
yt = pytube.YouTube(link)
yt.streams.first().download()
print('Downloaded',link)
