import yt_dlp
import sys 

if len(sys.argv) != 2:
    print("needs two arguments")
    sys.exit(1)
url = sys.argv[1]

try:
    ydl_options = {'skip_download': True, 'quiet': True}
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        metadata = ydl.extract_info(url, download=False)
        title = metadata.get('title')
        print(f"title: {title}")
except yt_dlp.utils.DownloadError:
    sys.exit(1)
answer = input("install video? y/n:  ")
if answer.lower() == "y":
    with yt_dlp.YoutubeDL() as ydl:
        ydl.download(url)

elif answer.lower() == "n":
    print("Ok wish you good day!")
    sys.exit(0)

else:
    print("um.. not really an option so..ABORT!")
    sys.exit(1)
