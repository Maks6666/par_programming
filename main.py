# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки.
# Перший потік знаходить суму елементів у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран.

import threading

def summa(lst):
    res = 0
    for i in lst:
        res += i
    print(res)

def medium(lst):
    res = 0
    for i in lst:
        res += i

    mid = res / len(lst)
    print(mid)

def create_list(num):
    lst = []
    for i in range(num):
        number = int(input(f"Input {i+1}st number: "))
        lst.append(number)
    t1 = threading.Thread(target=summa, args=(lst,))
    t2 = threading.Thread(target=medium, args=(lst,))

    t1.start()
    t2.start()

    return t1, t2


print(create_list(4))