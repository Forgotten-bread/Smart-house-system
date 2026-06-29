import random as r
import time
def light_control():
    print("\nУправление светом")
    command = input("Введите команду (включить/выключить/авто): ").lower()
    if command == "включить":
        print("Свет включен.")
    elif command == "выключить":
        print("Свет выключен.")
    elif command == "авто":
        time = r.randint(0, 23)
        minute = r.randint(0, 59)
        if 6 <= time <= 18:
            print(f"Сейчас {time}:{minute}")
            print("Свет выключен.(День)")
        else:
            print(f"Сейчас {time}:{minute}")
            print("Свет включен.(Ночь)")
    else:
        print("Команда не распознана!")

def temp_control():
    print("\nУправление отоплением и кондиционером")
    while True:
        x = r.randint (15, 35)
        if x%10 <= 4 and x%10 > 1:
            a = ' градуса.'
        elif x%10 == 1:
            a = ' градус.'
        else:
            a = ' градусов.'
        print('Температура воздуха ' + str(x) + a)
        if x > 24:
            print('Слишком жарко, уменьшаю обогрев помещения.')
            while x > 24:
                x = x - 1
                time.sleep(1)
                if x%10 <= 4 and x%10 > 1:
                    b = ' градуса.'
                elif x%10 == 1:
                    b = ' градус.'
                else:
                    b = ' градусов.'
                print('Текущая температура помещения ' + str(x) + b)
            print('Температура в норме.')
        elif x < 24:
            print('Слишком прохладно, усиливаю обогрев помещения.')
            while x < 24:
                x = x + 1
                time.sleep(1)
                if x%10 <= 4 and x%10 > 1:
                    c = ' градуса.'
                elif x%10 == 1:
                    c = ' градус.'
                else:
                    c = ' градусов.'
                print('Текущая температура помещения ' + str(x) + c)
            print('Температура в норме.')
        else:
            print('Температура в норме.')
        print('Продолжить отслеживать температуру воздуха? (y/n)')
        i = input()
        if i == 'n':
            print('Завершение работы...')
            break
        time.sleep(2)

def safety_check():
    print("\nПроверка безопасности")
    door_closed = input("Дверь закрыта? (да/нет): ").lower()
    window_closed = input("Окна закрыты? (да/нет): ").lower()
    if door_closed == "да" and window_closed == "да":
        print("Дом в безопасности.")
    else:
        print("Тогда закрой-_-")

print("Включение системы умного дома...")
time.sleep(2)
while True:
    print("1. Управление светом")
    print("2. Управление температурой")
    print("3. Проверка безопасности")
    print("4. Выйти")
    choice = int(input("Выберите действие (1-4): "))
    if choice == 1:
        light_control()
    elif choice == 2:
        temp_control()
    elif choice == 3:
        safety_check()
    elif choice == 4:
        print("Выход из системы умного дома. До свидания!")
        break
    else:
        print("Неверный выбор, попробуйте снова!")
