import math


def factorize(x):
    tab = []
    i = 2
    e = math.floor(math.sqrt(x))

    while (i <= e):
        while (x % i == 0):
            tab.append(i)
            x = x/i
            e = math.floor(math.sqrt(x))
        i += 1
    if (x > 1):
        tab.append(int(x))
    return tab


def lcm():
    nww = 1
    previous = 0
    tab192 = factorize(192)
    tab348 = factorize(348)
    for i in tab192:
        if(i != previous):
            a = tab192.count(i)
            b = tab348.count(i)
            if (a >= b):
                nww *= math.pow(i, a)
        previous = i

    previous = 0
    for i in tab348:
        if (i != previous):
            a = tab348.count(i)
            b = tab192.count(i)
            if (a > b):
                nww *= math.pow(i, a)
        previous = i

    return int(nww)


print(lcm())
