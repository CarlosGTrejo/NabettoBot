from functions.Bet import Bet, majorityBet
from random import choice, randint


test = []
user = ["James", "Minh", "Huy", "Carlos", "Thanh"]
team = ["BLUE", "RED"]
bet = 0 # for now
for i in range(10):
    test.append(Bet(choice(user), choice(team), randint(1, 1000)))

for item in test:
    print(item.user, item.team, item.bet_amount)

print(type(test[0]))
print(majorityBet(test, 10000))