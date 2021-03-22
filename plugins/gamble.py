import random

def hi_low():
    die1 = random.choice(range(1,6))
    die2 = random.choice(range(1,6))
    if (die1 + die2) < 7:
        return "low",die1+die2,die1,die2
    return "high",die1+die2,die1,die2
