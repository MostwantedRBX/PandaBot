import random

class LotteryDrawing:
    num = []

    def __init__(self):
        self.num = self.draw_numbers()

    def draw_numbers(self):
        num = random.sample(range(1,50),k=6)
        return sorted(num)
