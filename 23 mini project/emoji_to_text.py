import unicodedata

def emoji_to_text(text):
    parts = []
    for ch in text:
        name = unicodedata.name(ch, "")
        if name and ("FACE" in name or "HEART" in name or "EMOJI" in name or ord(ch) > 0x1F000):
            parts.append(f"[{name.lower().replace(' ', '_')}]")
        else:
            parts.append(ch)
    return "".join(parts)

if __name__ == "__main__":
    print(emoji_to_text(input("Text with emoji: ")))
