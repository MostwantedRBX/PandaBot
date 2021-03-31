# import schedule
# import time

# from lottery.controller import LotteryController
# from discord import Webhook, RequestsWebhookAdapter

# def job():
#     dc = LotteryController()
#     numbers = dc.draw_numbers()
#     num_str = ",".join(str(numbers))
#     print(numbers)
#     uid=825124651809767465
#     token = '8XIk8n6pCiBB1AA91ntMR4VH-GtztbiYDViz_B1omnOLWeZotCsdUDzf9X9TZDaskgpf'
#     webhook = Webhook.partial(uid,token,adapter=RequestsWebhookAdapter())
#     webhook.send(num_str,username='Lottery Keeper')
    
    
# schedule.every(5).seconds.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)