import yt_dlp
import os
import glob
import uuid

def download_instagram(url):
    # unique folder for each request
    uid = str(uuid.uuid4())[:8]
    base_dir = f"downloads/insta_{uid}"
    os.makedirs(base_dir, exist_ok=True)

    ydl_opts = {
        "outtmpl": f"{base_dir}/%(id)s_%(index)s.%(ext)s",
        "cookiefile": "cookies.txt",
        "quiet": True,
        "merge_output_format": "mp4",
        "extractor_args": {
            "instagram": {
                "include_ads": False
            }
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=True)

        # collect ALL files (jpg, mp4, webp etc)
        files = sorted(
            glob.glob(f"{base_dir}/*")
        )

        return files if files else None

    except Exception as e:
        print("Insta error:", e)
        return None
