import random
import time

print("Добро пожаловать в игру 'Угадай число'!")
time.sleep(1)
print("Для старта игры введите число, в пределах которго я буду загадывать, а вы угадывать.")
time.sleep(2)

top_of_range = input("Начнем! Введите число больше нуля: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Нужно число больше нуля.")
        quit()
else:
    print("Нужно ввести число.")
    quit()

random_number = random.randint(0, top_of_range)

while True:
    user_guess = input("Какое число я загадал? ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess > top_of_range:
            print("Вы ввели число, выходящее за пределы.")
            continue
    else:
        print("Введите число.")
        continue

    if user_guess == random_number:
        print("Вы угадали!")
        break
    else:
        if user_guess > random_number:
            print("Число меньше.")
        else:
            print("Число больше.")
