def blackjack(score):
    if score == 21:
        return "Blackjack!"
    elif score > 21:
        return "Bust!"
    elif score >= 17 and score < 21:
        return "Nice hand!"
    else:
        return "Hit me!"
    
print(blackjack(21))
print(blackjack(24))
print(blackjack(19))
print(blackjack(10))