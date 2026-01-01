import yt_dlp
import os

def download_youtube(url):
    os.makedirs("downloads", exist_ok=True)

    ydl_opts = {
        "outtmpl": "downloads/yt_%(id)s.%(ext)s",
        "format": "bestaudio/best",
        "cookiefile": "cookies.txt",
        "quiet": True,
        "noplaylist": True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info)
    except Exception as e:
        print("YT ERROR:", e)
        return None
