calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    a = tuple([len(string), string.upper(), string.lower()])
    return a


def is_contains(string, list_to_search):
    count_calls()
    flag = False
    string = string.upper()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].upper()
        if string in list_to_search[i]:
            flag = True
            break
    return flag


print(string_info('tolsTOY'))
print(string_info('MarSHMELLO'))
print(string_info('Rein'))
print(is_contains('LE', ['SmolenSK', 'Lena', 'Lensk', 'OlesiA']))
print(is_contains('ea', ['WarAndPEACE', 'eATH', 'leaVe', 'Mikhail']))
print(is_contains('First', ['quires', 'vous', 'savez', 'loPUKHIn']))
print(calls)
