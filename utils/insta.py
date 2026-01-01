import instaloader

def download_instagram(url):
    try:
        L = instaloader.Instaloader(dirname_pattern="downloads", save_metadata=False)
        shortcode = url.split("/")[-2]
        L.download_post(instaloader.Post.from_shortcode(L.context, shortcode), target="insta")
        return None
    except:
        return None
