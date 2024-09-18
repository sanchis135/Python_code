# Task 5: Concatenate dictionaries

def concatDic(d1, d2):
    d1.update(d2)
    return d1

dic1 = {'a': 2, 'b': 6}
dic2 = {'c': 1, 'd': 7}

print(concatDic(dic1, dic2))