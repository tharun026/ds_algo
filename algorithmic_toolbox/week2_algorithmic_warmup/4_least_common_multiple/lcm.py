# Uses python3
import sys

def lcm_naive(a, b):
    if a == 0 or b == 0:
        return 0

    for i in range(1, b + 1):
        if (i * a) % b == 0:
            return i * a

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

