from models.Fetch import fetchSettings

class Bet:
    """The class stores all basic information collected from each betting session."""
    def __init__(self, user, team, bet_amount): # Constructor
        self.user: "Bet person" = user
        self.team: "Team the person bet" = team
        self.bet_amount: "Amount person bet" = bet_amount

def betExtract(message):
    """This function extracts data from messages and return a list that has all the data."""
    split_point: "Point to split the message" = "PRIVMSG #" + fetchSettings().CHANNEL + " :"
    # Extract username
    username = message.split(split_point)[0].split("!")[0].strip(":")
    # Extract team
    team = "BLUE" if "BLUE" in message else "RED"
    # Extract amount
    amount = int(message.split('-').pop().split('.').pop(0).split(', ')[1])
    return [username, team, amount]


def majorityBet(bets, current_amount):
    """This function takes data from a Bet class list and the current balance.
    It returns a bet statement based on the team with the most money and the
    current amount of money the owner has."""
    
    blue, red = 0, 0 # assume bet cannot be a negative number
    final_bet_amount: "Current amount * 0.1" = current_amount * 0.1 # each bet is 10% of the total amount owned

    # Sort and add bets to two baskets: red and blue
    for bet in bets:
        if (bet.team == "BLUE"):
            blue += bet.bet_amount  
        else:
            red += bet.bet_amount

    # Make the final betting decision based on the majority bet
    if (blue > red):
        return "!blue " + str(int(final_bet_amount)) # convert the bet amount to an int because the betting bot only accepts whole numbers
    else:
        return "!red " + str(int(final_bet_amount)) 

def sideWithMoreMoney(bets):

    blue, red = 0, 0 # assume bet cannot be a negative number

    # Sort and add bets to two baskets: red and blue
    for bet in bets:
        if (bet.team == "BLUE"):
            blue += bet.bet_amount  
        else:
            red += bet.bet_amount

    # Make the final betting decision based on the majority bet
    print("BLUE:", blue, "RED:", red)