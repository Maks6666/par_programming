# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки.
# Перший потік знаходить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.

import threading

def maximum(lst):
    print(max(lst))

def minimum(lst):
    print(min(lst))

def create_list(num):
    lst = []
    for i in range(num):
        number = int(input(f"Input {i+1}st number: "))
        lst.append(number)
    t1 = threading.Thread(target=maximum, args=(lst,))
    t2 = threading.Thread(target=minimum, args=(lst,))

    t1.start()
    t2.start()

    return t1, t2


print(create_list(4))