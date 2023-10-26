from decouple import config
from logic import play_bet
balance = config("MyMoney", cast=int)

while True:
    bet = int(input(f'Сколько вы хотите поставить? (Баланс: {balance})'))
    lot = int(input(f'Лот на который хотите паставить (1-30)'))
    if bet < 1 or bet > balance:
        print('Неправильная сумма ставки')
        continue
    if lot < 1 or lot > 30:
        print('Неправильный лот')
        continue
    balance += play_bet(bet, lot)
    if balance == 0:
        print('У вас кончились деньги!')
        break
    answer = input('Вы хотите продолжить? (Y/N)')
    if answer == 'N':
        break
