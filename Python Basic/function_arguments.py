"""Positional, keyword, default, *args, and **kwargs arguments."""
def profile(name, country="Bangladesh", *skills, **details):
    return {"name": name, "country": country, "skills": skills, "details": details}

print(profile("Noman", "Bangladesh", "Python", "C", level="beginner"))
