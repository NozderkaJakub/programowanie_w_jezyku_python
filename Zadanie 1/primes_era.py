import math


def eratostenes(liczba):
    tab = list(range(2, liczba+1))       #   tab = [True for _ in range(liczba)]     # może być również tak albo: tab = [True] * liczba co będzie o wiele szybsze

    for x in tab[:int(math.sqrt(liczba))-1]:
        if x:                         #     if x is not None: # uzywa sie gdy w tablicy są zera bo są ewaluowane na False, None też na False
            for k in range(2*x-2, liczba-1, x):
                tab[k] = None                 #   None jest singletonem

    # for i in range(2, int(math.sqrt(liczba))):
    #     if tab[i-2]:
    #         for j in range(2*i, liczba + 1, i):
    #             tab[j-2] = False

    # numbers = []
    # for i in range(len(tab)):
    #     if (tab[i]):
    #         numbers.append(i+2)
    # return numbers

    # return [i for i in tab if i]

    prime_nums = list(filter(lambda x: x, tab))#prime_nums = list(filter(lambda x: x is not None, tab))
    return prime_nums
    

n = 100
print(eratostenes(n))
