import time
import json
import random
{"name": "Example","id": "1234","amount": "100000"}
def pick_winner(filepath="lotto.json"):
    with open(filepath) as f:
        data = json.load(f)
        return random.choice(data['entries'])

print(pick_winner())