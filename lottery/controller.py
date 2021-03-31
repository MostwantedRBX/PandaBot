#from .model import LotteryDrawing
import json
import math

def write_json(data,filename='./lottery/lotto.json'):
    print('writing')
    with open(filename,'w') as f:
        json.dump(data,f,indent=4)

def create_ticket(name,uid,amount):
    print('creating ticket')
    ticket=[
        {
            "name": name,
            "id": uid
        }
    ]
    if amount >= 100:
        with open("./lottery/lotto.json") as f:
            cost_of_ticket = 100
            data = json.load(f)
            temp = data['entries']
            for i in range(1,math.floor(amount/cost_of_ticket)+1):
                print(data)
                temp.append(ticket[0])
                write_json(data)
            return True
    else:
        print('Not Enough Money')
        return False

#class LotteryController:

    #def draw_numbers(self):
        #drawing = LotteryDrawing()
        #return drawing.num

def addTicket(name, uid, money):
    if create_ticket(name,uid,money):
        with open("./lottery/lotto.json") as f:
            data = json.load(f)
            data['pot'] = data['pot']+int(100*(math.floor(money/100)))
            write_json(data)
    

