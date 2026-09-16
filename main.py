import yt_dlp
import sys 

if len(sys.argv) != 2:
    print("needs two aurgments")
    sys.exit(1)
url = sys.argv[1]

ydl_options = {'skip_download': True, 'quiet': True}
with yt_dlp.YoutubeDL(ydl_options) as yoo:
    info = yoo.extract_info(url, download=False)
    title = info.get('title')
    print (title)
