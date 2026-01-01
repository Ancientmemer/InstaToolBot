import yt_dlp
import os
import glob

def download_instagram(url):
    os.makedirs("downloads", exist_ok=True)

    ydl_opts = {
        "outtmpl": "downloads/insta_%(id)s_%(index)s.%(ext)s",
        "format": "best",
        "cookiefile": "cookies.txt",
        "quiet": True,
        "noplaylist": True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=True)

        # collect all downloaded files
        files = sorted(glob.glob("downloads/insta_*"))
        return files if files else None

    except Exception as e:
        print("Insta error:", e)
        return None
