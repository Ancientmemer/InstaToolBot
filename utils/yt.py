import yt_dlp
import os
import uuid
import glob

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
    else:
        ydl_opts = {
            "outtmpl": f"downloads/yt_{uid}.%(ext)s",
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "quiet": True,
            "noplaylist": True,
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=True)

        # 🔑 FIND ACTUAL OUTPUT FILE
        if mode == "audio":
            files = glob.glob(f"downloads/yt_{uid}*.mp3")
        else:
            files = glob.glob(f"downloads/yt_{uid}*.mp4")

        return files[0] if files else None

    except Exception as e:
        print("YT error:", e)
        return None
