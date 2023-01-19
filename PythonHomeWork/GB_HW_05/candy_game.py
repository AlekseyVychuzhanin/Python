# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

from random import randint as ri

total_candy = 250
candy_taken = 0
player_1_sweet = 0
player_2_sweet = 0
max_take = 28

player_1 = input('Введите имя первого игрока: ')
# player_2 = input('Введите имя второго игрока: ')

def start_game():
    print('На столе лежит заданное количество конфет. \nИграют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. \nЗа один ход можно забрать не более чем 28 конфет. \nВсе конфеты оппонента достаются сделавшему последний ход.')

    who_is_first()

def who_is_first():
    random_number = ri(1, 2)
    if random_number == 1:
        player_1_turn()
    else:
        # player_2_turn()
        bot_turn()

def player_1_turn():
    global total_candy
    global candy_taken
    global player_1_sweet
    print(f'Ходит {player_1}, сейчас на столе {total_candy} конфет')
    candy_taken = int(input('Сколько конфет вы берете?: '))
    while candy_taken > max_take or candy_taken < 0 or candy_taken > total_candy:
        candy_taken = int(input('Некорректное количество конфет! Попробуйте снова: '))
    total_candy -= candy_taken
    player_1_sweet += candy_taken
    if total_candy > 0:
        # player_2_turn()
        bot_turn()
    else:
        print(f'{player_1} Победил')

# def player_2_turn():
#     global total_candy
#     global candy_taken
#     global player_2_sweet
#     print(f'Ходит {player_2}, сейчас на столе {total_candy} конфет')
#     candy_taken = int(input('Сколько конфет вы берете?: '))
#     while candy_taken > max_take or candy_taken < 0 or candy_taken > total_candy:
#         candy_taken = int(input('Некорректное количество конфет! Попробуйте снова: '))
#     total_candy -= candy_taken
#     player_2_sweet += candy_taken
#     if total_candy > 0:
#         player_1_turn()
#     else:
#         print(f'{player_2} Победил')

def bot_turn():
    global total_candy
    global candy_taken
    global player_2_sweet
    candy_taken = total_candy % 29 if total_candy % 29 != 0 else ri(1, 28)
    total_candy -= candy_taken
    player_2_sweet += candy_taken
    print(f'Бот взял {candy_taken} конфет!')
    if total_candy > 0:
        player_1_turn()
    else:
        print('Бот победил!')

start_game()