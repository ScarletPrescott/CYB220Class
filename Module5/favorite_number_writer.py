#ScarletPrescott
import json

filename = 'favorite_number.json'

favorite_number = input("What's your favorite number? ")

with open(filename, 'w') as file:
    json.dump(favorite_number, file)

print("Thanks! I'll remember that.")
