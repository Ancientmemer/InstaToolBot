import random

def smart_reply(text):
    text = text.lower()
    if "hi" in text or "hello" in text:
        return random.choice(["Hey 👋", "Hello 😄"])
    if "bored" in text:
        return "😴 Same feeling… send a reel link!"
    if "thanks" in text:
        return "❤️ Anytime bro!"
    return None
