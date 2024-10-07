def single_root_words(root_word,  *other_words):
    same_words = []
    a = root_word.upper()
    for word in other_words:
        if word.upper() in a or a in word.upper():
            same_words.append(word)
        else:
            continue
    return same_words



result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)