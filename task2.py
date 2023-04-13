# Задача 12: Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# Пример:
# Ввод: 5 6 -> 2 3


from math import sqrt
from math import floor

flag = 1
num_sum = int(input())
num_prod = int(input())
while flag:
    if (num_sum < 2 or num_prod < 0):
        print("one of numbers is not natural, try again:")
        num_sum = int(input())
        num_prod = int(input())
    elif(num_sum >= 1001 or num_prod >= 1001):
        print("one of numbers is more than 1000, try again:")
        num_sum = int(input())
        num_prod = int(input())
    else:
        flag = 0

D = pow(num_sum,2) - 4 * num_prod
if(D > 0):
    temp_x = floor((num_sum + sqrt(D)) / 2)
elif(D == 0):
    temp_x = num_sum / 2
else:
    print("n/a")

if (D >= 0):
    x1 = num_sum - temp_x
    y1 = num_sum - x1

    x2 = num_prod / temp_x
    y2 = num_prod / x2

    if (x1 == x2 and y1 == y2):
        print(int(x1))
        print(int(y1))
    else:
        print("n/a")
    

