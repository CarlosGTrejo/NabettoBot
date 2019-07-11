# from models.Bet import Bet, majorityBet
# from random import choice, randint


# test = []
# user = ["James", "Minh", "Huy", "Carlos", "Thanh"]
# team = ["BLUE", "RED"]
# bet = 0 # for now
# for i in range(10):
#     test.append(Bet(choice(user), choice(team), randint(1, 1000)))

# for item in test:
#     print(item.user, item.team, item.bet_amount)

# print(majorityBet(test, 10000))

from time import perf_counter, sleep


while True:
    print(perf_counter())
    if (int(perf_counter()) % 120 == 0):
        print("Hello!")
    sleep(1)
        