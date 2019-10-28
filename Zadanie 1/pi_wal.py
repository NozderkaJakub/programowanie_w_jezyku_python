def wallis(n):
    if (n >= 1):
        return (((2*n)*(2*n)) / ((2*n-1)*(2*n+1))) * wallis(n-1)  # dobrze by było uprościć kod, wspolne mianowniki do zmiennej, i*i jest szybsze niż i**2
    else:
        return 2.0  # ponieważ wynik końcowy to pi/2, wynikiem dzielenia jest liczba zmiennoprzecinkowa więc *2.0 będzie szybsze niż *2


if __name__ == "__main__":
    n = 10
    for x in range(1, n + 1):
        print(wallis(x))


# można uruchomić jako: ' python3 -m timeit -s "import pi_wal" "pi_wal.wallis(10)" ' żeby zmierzyć czas, -m przeszukuje standardowe ścieżki w poszukiwaniu modułu