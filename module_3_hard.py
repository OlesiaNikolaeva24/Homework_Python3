def calculate_structure_sum(*args, total=0):
    for arg in args:
        if isinstance(arg, dict):
            for d in list(arg.items()):
                total += calculate_structure_sum(d)
        elif isinstance(arg, list) or isinstance(arg, tuple) or isinstance(arg, set):
            for element in arg:
                total += calculate_structure_sum(element)
        elif isinstance(arg, str):
            total += len(arg)
        elif isinstance(arg, int):
            total += arg
    return total


# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
