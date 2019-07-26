from nabettobot.functions.Tools import logBet
from nabettobot.models.Connection import settings


class Bet:
    """The class stores all basic information collected from each betting session."""

    __static_data__: "Holds the total bet amount for each team" = {"BLUE":0, "RED":0}

    def __init__(self, user, team, bet_amount): # Constructor
        self.user: "Person that placed the bet" = user
        self.team: "Team the person bet on" = team
        self.bet_amount: "Amount person bet" = bet_amount

        __static_data__[self.team] += self.bet_amount # Adding bet amount to the appropriate team.

    @staticmethod
    def reset() -> None:
        """Resets the data variable to {BLUE:0, RED:0} for the next betting session"""
        Bet.__static_data__.update(BLUE=0, RED=0) # Resetting the data variable.

    @classmethod
    def extractBet(cls,message: "A betting request message") -> "Bet Object":
        """Extracts bet data from a message and updates the __static_data__ variable based on the chosen team"""
        split_point: "Where the message is split" = "PRIVMSG #" + settings.CHANNEL + " :"
        # Extract username
        username = message.split(split_point)[1].split("@")[1].split(" - ")[0]
        # Extract team
        team = "BLUE" if "BLUE" in message else "RED"
        # Extract amount
        amount = int(message.split('-').pop().split('.').pop(0).split(', ')[1])
        bet_info = (username, team, amount)
        logBet(bet_info)

        return cls(*bet_info)

    @staticmethod
    def betWithMajority(current_amount: "The current amount of money you hold") -> "!(team) str(current_amount * 0.1)":
        """Returns a bet command based on the team that holds the highest bet"""
        return f"!{max(__static_data__).lower} {current_amount * 0.1}"
