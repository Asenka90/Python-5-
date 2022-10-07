#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

print('***Задача 1***')
text = 'забвение ручка зимбабве кружка абвер'
print(text)
print(' '.join(list(filter(lambda word: not word.__contains__('абв'), text.split()))))

#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
#За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

print('***Задача 2***')
from random import randint
сandies = 2021
m = 28
def game(Q, step):
    i = randint(1, 2)
    j = 2
    if i == j:
        j = 1
    while Q > 0:
        winner = ""
        if Q > 0 and Q <= step:
            user1 = Q
        else:
            user1 = randint(1, step)
        Q = Q - user1
        print(Q , i, end = ' ')
        if Q == 0:
            winner = "Выиграл игрок №" + str(i)
        if Q > 0 and Q <= step:
            user2 = Q
        else:
            user2 = randint(1, step)
        Q = Q - user2
        print(Q, j, end = ' ')
        if Q == 0:
            winner = "Выиграл игрок  №" + str(j)
    return winner
print(game(сandies, m))

#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""

print('***Задача 3***')
def game2(Q, step):
    winner2 = ""
    i = randint(1, 2)
    print(i)
    while Q > 0:
        if i == 1:                     
            if Q <= step:
                human = Q
            else:
                human = randint(1, step)
            Q = Q - human
            print(Q, "человек", end = ' ')
            if Q == 0:
                winner2 = "Выиграл человек"                      
            bot = Q % (step + 1)
            if bot == 0:
                bot = randint(1, step)
            Q = Q - bot
            print(Q, end = ' ')
            if Q == 0:
                winner2 = "Выиграл bot"
        else:                        
            bot = Q % (step + 1)
            Q = Q - bot
            print(Q, end = ' ')
            if Q == 0:
                winner2 = "Выиграл bot"
            human = randint(1, step)
            Q = Q - human
            print(Q, end = ' ')
            if Q == 0:
                winner2 = "Выиграл человек"
    return winner2

print(game2(сandies, m))

#Создайте программу для игры в ""Крестики-нолики"".

print('***Задача 4***')
board = list(range(1,10))
def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")
def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False
def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)
main(board)

#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.

print('***Задача 5***')
file1 = open("исходная строка.txt", "r")
lines = file1.readlines()
file1.close()
for line in lines:
    print(line.strip())
def encode(s):
    encoding = "" 
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1
    return encoding
#print(encode(s))
for line in lines:
    print(encode(line.strip()))
text_file = open("полученная строка.txt", "w")
n = text_file.write(encode(line.strip()))
text_file.close()