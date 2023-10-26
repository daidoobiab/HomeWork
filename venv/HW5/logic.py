import random

def play_bet(bet, lot):
    win_lot = random.randint(1, 31)
    if lot == win_lot:
        print("ВЫ ВИГРАЛИ!")
        return bet * 2
    else:
        print("ВЫ ПРОИГРАЛИ!")
        return -bet


