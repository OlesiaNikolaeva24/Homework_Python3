def calculate_structure_sum(*args):
    global summa
    if not len(args) > 1:
        if isinstance(args, str):
            summa += len(args)
        elif isinstance(args, int):
            summa += args
        else:
            continue
    for i in args:
        calculate_structure_sum(*args)


summa = 0

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

print(summa)
