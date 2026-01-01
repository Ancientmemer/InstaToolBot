import yt_dlp
import os
import uuid

def download_youtube(url, mode="video"):
    os.makedirs("downloads", exist_ok=True)
    uid = str(uuid.uuid4())[:8]

    if mode == "audio":
        ydl_opts = {
            "outtmpl": f"downloads/yt_{uid}.%(ext)s",
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "quiet": True,
            "noplaylist": True,
        }
    else:  # video
        ydl_opts = {
            "outtmpl": f"downloads/yt_{uid}.%(ext)s",
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "quiet": True,
            "noplaylist": True,
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info)
    except Exception as e:
        print("YT error:", e)
        return None
