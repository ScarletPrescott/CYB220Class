#ScarletPrescott
from pathlib import Path
import json

path = Path('favorite_number.json')
try:
    contents = path.read_text()
except FileNotFoundError:
    number = input("What's your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("I'll remember that.")
else:
    number = json.loads(contents)
    print(f"I know your number, it's {number}")
