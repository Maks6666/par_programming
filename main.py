# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.

import threading
import pickle

def create_file():
    file_name = input("Input file name: ")
    data = []
    numbers = int(input("Input length of the list: "))
    for i in range(numbers):
        num = int(input(f"Input {i+1}st number: "))
        data.append(num)
    with open(f"{file_name}.pickle", "wb") as file:
        pickle.dump(data, file)
    return "Data saved."

def even_numbers(file_name, new_file_name):
    with open(file_name, "rb") as file:
        read_data = pickle.load(file)
    if len(read_data) > 0:
        even_numbers_list = []
        for i in read_data:
            if i % 2 == 0:
                even_numbers_list.append(i)
        with open(f"{new_file_name}.pickle", "wb") as file:
            pickle.dump(even_numbers_list, file)
        print(even_numbers_list)


def non_even_numbers(file_name, new_file_name):
    with open(file_name, "rb") as file:
        read_data = pickle.load(file)
    if len(read_data) > 0:
        non_even_numbers_list = []
        for i in read_data:
            if i % 2 != 0:
                non_even_numbers_list.append(i)
        with open(f"{new_file_name}.pickle", "wb") as file:
            pickle.dump(non_even_numbers_list, file)
        print(non_even_numbers_list)


create_file()
t1 = threading.Thread(target=even_numbers, args=('data.pickle', 'even_num_data'))
t2 = threading.Thread(target=non_even_numbers, args=('data.pickle', 'non_even_num_data'))

t1.start()
t2.start()

t1.join()
t2.join()
