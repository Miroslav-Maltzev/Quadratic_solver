import math


def solve(a, b, c):
    d = dis(a, b, c)
    if d > 0:
        x1 = -b+math.sqrt(d)/2*a
        x2 = -b-math.sqrt(d)/2*a
    else:
        print('Нет корней!')
        return
    return [x1, x2]


def dis(a, b, c):
    return b**2-4*a*c


"ax**2+bx+c=0"
a = int(input('Введите a\n--->'))
b = int(input('Введите b\n--->'))
c = int(input('Введите c\n--->'))
print(f"{a}x*x{'' if b < 0 else '+'}{b}x{'' if c < 0 else '+'}{c}")

print(solve(a, b, c))