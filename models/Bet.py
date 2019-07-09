# Betting class
class Bet:
    """The class stores all basic information collected from each betting session."""
    def __init__(self, user, team, bet_amount): # Constructor
        self.user: "Bet person" = user
        self.team: "Team the person bet" = team
        self.bet_amount: "Amount person bet" = bet_amount
    

