from pytube import YouTube

print("Welcome to Novachrono\'s YouTube Downloader")

link = str(input("Enter YouTube link: "))
yt = YouTube(link)

# print(yt.streams)
print(f"Title: {yt.title} \nLength of video: {yt.length} seconds")

stream = yt.streams.get_by_resolution("360p")
stream.download()

print("Download Successful!!!")