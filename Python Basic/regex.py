"""Regular expressions."""
import re
text = "Contact: example@example.com"
match = re.search(r"[\w.-]+@[\w.-]+", text)
if match:
    print(match.group())
