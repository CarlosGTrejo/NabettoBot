class Bet:
    """The class stores all basic information collected from each betting session."""
    def __init__(self, user, team, bet_amount): # Constructor
        self.user: "Bet person" = user
        self.team: "Team the person bet" = team
        self.bet_amount: "Amount person bet" = bet_amount
    
def majorityBet(bets, current_amount):
    """This function takes data from a Bet class list and the current balance.
    It returns a bet statement based on the team with the most money and the
    current amount of money the owner has."""
    
    blue, red = 0, 0 # assume bet cannot be a negative number
    final_bet_amount: "Current amount * 0.1" = current_amount * 0.1

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