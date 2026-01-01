import yt_dlp
import os
import uuid
import glob
import time

def download_instagram(url):
    time.sleep(2)

    uid = str(uuid.uuid4())[:8]
    base_dir = f"downloads/insta_{uid}"
    os.makedirs(base_dir, exist_ok=True)

    ydl_opts = {
        "outtmpl": f"{base_dir}/%(id)s.%(ext)s",
        "cookiefile": "cookies.txt",
        "quiet": True,

        # 🔑 THE MAGIC FLAGS
        "ignoreerrors": True,
        "ignore_no_formats_error": True,
        "allow_unplayable_formats": True,

        # 🔑 PHOTO SUPPORT
        "write_thumbnail": True,
        "skip_download": False,

        "http_headers": {
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; Mobile)",
            "Accept-Language": "en-US,en;q=0.9"
        },

        "extractor_args": {
            "instagram": {
                "include_ads": False
            }
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=True)

        # collect ALL media (mp4 + jpg + webp)
        files = []
        files.extend(glob.glob(f"{base_dir}/*.mp4"))
        files.extend(glob.glob(f"{base_dir}/*.jpg"))
        files.extend(glob.glob(f"{base_dir}/*.jpeg"))
        files.extend(glob.glob(f"{base_dir}/*.png"))
        files.extend(glob.glob(f"{base_dir}/*.webp"))

        return files if files else None

    except Exception as e:
        print("Insta error:", e)
        return None
