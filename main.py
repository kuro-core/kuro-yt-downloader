import yt_dlp
import sys 

if len(sys.argv) != 2:
    print("needs two aurgments")
    sys.exit(1)
url = sys.argv[1]
    
    ydl_options = {'skip_download': True, 'quiet': True}
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        info = ydl.extract_info(url, download=False)
        title = info.get('title')
        print(title)

answer = input("install video? y/n:  ")
if answer.lower() == "y":
    with yt_dlp.YoutubeDL() as ydl:
        ydl.download(url)

elif answer.lower() == "n":
    print("Ok wish you good day!")
    sys.exit(0)

else:
    print("um.. not really an option so..ABORT!")
    sys.exit(0)
