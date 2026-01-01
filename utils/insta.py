import os
import time
import uuid
import glob
import yt_dlp
import instaloader

def download_instagram(url):
    time.sleep(2)

    uid = str(uuid.uuid4())[:8]
    base_dir = f"downloads/insta_{uid}"
    os.makedirs(base_dir, exist_ok=True)

    # --------- TRY VIDEO FIRST (yt-dlp) ---------
    ydl_opts = {
        "outtmpl": f"{base_dir}/video.%(ext)s",
        "format": "bv*+ba/best",
        "merge_output_format": "mp4",
        "quiet": True,
        "cookiefile": "cookies.txt",
        "retries": 2,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=True)

        videos = glob.glob(f"{base_dir}/*.mp4")
        if videos:
            return videos
    except:
        pass

    # --------- FALLBACK TO PHOTO (instaloader) ---------
    try:
        L = instaloader.Instaloader(
            dirname_pattern=base_dir,
            save_metadata=False,
            download_comments=False,
            quiet=True
        )

        shortcode = url.rstrip("/").split("/")[-1]
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
