import yt_dlp
import os

def download_youtube(url):
    os.makedirs("downloads", exist_ok=True)

    ydl_opts = {
        "outtmpl": "downloads/yt_%(id)s.%(ext)s",
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "cookiefile": "cookies.txt",
        "quiet": True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info)
    except Exception as e:
        print("YT error:", e)
        return None
