import sys

def eratostenes(tab):
    for x in range(99):
        tab.append(True)

    for i in range(2, 11):
        if tab[i-2] == True:
            for j in range (2*i, 101, i):
                tab[j-2] = False

numbers = []
eratostenes(numbers)
for i in range(len(numbers)):
    if(numbers[i] == True):
        print(i+2)