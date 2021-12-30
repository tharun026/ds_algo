# Uses python3

def calc_fib(n):
    if n == 0:
        return 0
    else:
        n1 = 0
        n2 = 1

        for i in range(2, n+1):
            n2, n1 = n1 + n2, n2
        return n2

n = int(input())
print(calc_fib(n))
