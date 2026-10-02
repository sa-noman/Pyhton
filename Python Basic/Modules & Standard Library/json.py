"""JSON encoding and decoding."""
import json
data = {"name": "Python", "type": "language"}
encoded = json.dumps(data)
decoded = json.loads(encoded)
print(encoded)
print(decoded["name"])
