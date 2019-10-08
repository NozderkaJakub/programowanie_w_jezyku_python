import sys

def wallis(n):
    if (n>=1):
        return (((2*n)*(2*n)) / ((2*n-1)*(2*n+1))) * wallis(n-1)
    else:
        return 2 #ponieważ wynik końcowy to pi/2

for x in range(1, int(sys.argv[1])+1):
    print(wallis(x))