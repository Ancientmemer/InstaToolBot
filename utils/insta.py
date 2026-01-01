import yt_dlp
import os

def download_instagram(url):
    os.makedirs("downloads", exist_ok=True)

    ydl_opts = {
        "outtmpl": "downloads/insta_%(id)s.%(ext)s",
        "format": "best",
        "cookiefile": "cookies.txt",
        "quiet": True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info)
    except Exception as e:
        print("Insta error:", e)
        return None
