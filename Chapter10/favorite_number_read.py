from pathlib import Path
import json

path = Path('favorite_number.json')
contents = path.read_text()
favorite_number = json.loads(contents)

print(f"I remember your favorite number, it's {favorite_number}!")
