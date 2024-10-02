def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()  # Передали значений 0
print_params('Python')  # Передали значений 1
print_params('Python', 3.12)  # Передали значений 2
print_params('Python', 3.12, 'UTF-8')  # Передали значений 3
print_params(b = 25)  # Переписали значение для b
print_params(c = [1,2,3])  # Переписали значение для c
print()
values_list = ['Terra', False, 6.09]  # Список - передает позиционные параметры
values_dict = {"b": 88, "c": False, "a": 'Tim'}  # Словарь - передает именованные параметры, ключи могут быть в любом порядке
print_params(*values_list)  # Распаковка списка
print_params(**values_dict)  # Распаковка словаря
print()
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # Распаковка списка + отдельный параметр
