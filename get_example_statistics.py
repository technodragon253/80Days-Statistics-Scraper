import os.path
import json

if os.path.exists('output.json'):
    pass
else:
    import get_data #Import calls all code that isn't in a function.

with open("output.json", "r") as f:
    raw_data = f.read()

data = json.loads(raw_data)

print(data["start_dates"])
