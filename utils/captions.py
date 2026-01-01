import random

def generate_caption(topic):
    captions = [
        f"Living the {topic} life 🔥",
        f"{topic.capitalize()} vibes only ✨",
        f"Enjoying every moment of {topic} 😍"
    ]
    hashtags = [
        f"#{topic}", "#reels", "#instagood", "#viral", "#explore"
    ]
    return random.choice(captions) + "\n\n" + " ".join(hashtags)
