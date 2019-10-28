def gcd(a, b):
    while b != 0: # while b:
        c = a % b  # a, b = b, a%b to jest to samo co a, b = b, c
        a = b
        b = c
    return a


if __name__ == "__main__":  #wykona się tylko przy wywołaniu tego modułu, dzięki czemu można importować (bez tego przy importowaniu wykonałby się cały moduł czyli by wypisał printa)
    print(gcd(84, 18))
