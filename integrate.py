import math
import sys


def abs_sin(x):
    return abs(math.sin(x))


def numerical_integral(lower, upper, N):
    width = (upper - lower) / N
    total = 0
    for i in range(N):
        x = lower + i * width
        total += abs_sin(x) * width
    return total


if __name__ == "__main__":
    lower = 0.0
    upper = 3.14159
    Ns = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    for N in Ns:
        result = numerical_integral(lower, upper, N)
        print(f"N={N}: {result}")
