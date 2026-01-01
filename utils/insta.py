import os
import time
import uuid
import glob

import yt_dlp
import instaloader


# 🔴 CHANGE THIS TO YOUR INSTAGRAM USERNAME
IG_USERNAME = "memer_in_realms"


# 🔑 REMOVE igsh / tracking params
def clean_instagram_url(url: str) -> str:
    return url.split("?")[0]


def download_instagram(url):
    # clean the URL first (VERY IMPORTANT)
    url = clean_instagram_url(url)

    # small delay to avoid rate limits
    time.sleep(2)

    uid = str(uuid.uuid4())[:8]
    base_dir = f"downloads/insta_{uid}"
    os.makedirs(base_dir, exist_ok=True)

    # ==================================================
    # 1️⃣ TRY VIDEO FIRST (REELS / VIDEO POSTS) – yt-dlp
    # ==================================================
    ydl_opts = {
        "outtmpl": f"{base_dir}/video.%(ext)s",
        "format": "bv*+ba/best",
        "merge_output_format": "mp4",
        "quiet": True,
        "retries": 2,
        "cookiefile": "cookies.txt",  # optional but helps
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=True)

        videos = glob.glob(f"{base_dir}/*.mp4")
        if videos:
            return videos

    except Exception:
        # if no video, continue to photo fallback
        pass

    # ==================================================
    # 2️⃣ PHOTO POSTS / CAROUSEL PHOTOS – instaloader
    # ==================================================
    try:
        L = instaloader.Instaloader(
            dirname_pattern=base_dir,
            save_metadata=False,
            download_comments=False,
            quiet=True,
        )

        # 🔑 LOAD SAVED LOGIN SESSION (OPTION 1)
        L.load_session_from_file(
            IG_USERNAME,
            filename=f"/data/data/com.termux/files/home/.config/instaloader/session-{IG_USERNAME}"
        )

        # extract shortcode safely
        parts = url.rstrip("/").split("/")
        shortcode = parts[-1]

        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target=base_dir)

        images = []
        images.extend(glob.glob(f"{base_dir}/*.jpg"))
        images.extend(glob.glob(f"{base_dir}/*.jpeg"))
        images.extend(glob.glob(f"{base_dir}/*.png"))

        return images if images else None

    except Exception as e:
        print("Insta error:", e)
        return None
