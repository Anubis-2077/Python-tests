rules = {
    ("rock", "scissors"): ("Player 1 wins!"),
    ("paper", "rock"): ("Player 1 wins!"),
    ("scissors", "paper"): ("Player 1 wins!"),
    ("rock", "paper"): ("Player 2 wins!"),
    ("paper", "scissors"): ("Player 2 wins!"),
    ("scissors", "rock"): ("Player 2 wins!"),
}


def rps(p1, p2):
    if p1 == p2:
        return "Draw!"

    return rules.get((p1, p2), "Invalid move!")


print(rps("rock", "paper"))  # Output: wins!
