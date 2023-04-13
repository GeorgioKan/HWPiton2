# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# С клавиатуры вводятся число монет и сами монеты построчно.

# Пример:
# Ввод: 1 1 1 1 0 0 -> 2

number_of_coins = int(input())
first_counter = 0
second_counter = 0
flag = 1

for i in range(number_of_coins):
    value = int(input())
    if(value == 0):
        first_counter += 1
    elif(value == 1):
        second_counter +=1
    else:
        print("n/a")
        flag = 0
        break

if (flag == 1):
    if(first_counter > second_counter):
        print(second_counter)
    else:
        print(first_counter)