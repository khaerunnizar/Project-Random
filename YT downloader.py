print ("Welcome To Python Youtube Downloader")

from pytube import YouTube
#import PIP pytube

link = input("Enter Youre Youtube URL :")
yt = YouTube(link)
videos = yt.streams.all()
#Menampilkan format video yang tersedia

video =list(enumerate(videos))
for i in video:
    print(i)
print("Enter the deisred option to download format")
dn_option = int(input("Enter the option :"))
#perintah input format video yang diinginkan

dn_video = videos[dn_option]
dn_video.download()
print("Downloaded Succesfully")