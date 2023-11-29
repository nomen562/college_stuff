# def bernoulli(n):
#     if n == 0:
#         return 1
#     else:
#         bernoulli_numbers = [0] * (n + 1)
#         bernoulli_numbers[0] = 1
#         for m in range(1, n + 1):
#             bernoulli_numbers[m] = 0
#             for k in range(m):
#                 bernoulli_numbers[m] += comb(m + 1, k) * bernoulli_numbers[k]
#             bernoulli_numbers[m] /= -(m + 1)
#         return bernoulli_numbers[-1]


# def comb(n, k):
#     if 0 <= k <= n:
#         result = 1
#         for i in range(1, min(k, n - k) + 1):
#             result *= n
#             result //= i
#             n -= 1
#         return result
#     else:
#         return 0


# if __name__ == "__main__":
#     for i in range(10):
#         print(f"B_{i} = {bernoulli(i)}")
import math


def maclaurin_series_tan(x, n):
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (2 * i + 1)
        print(term)
        result += term
    return result


# Example usage:
x = math.pi / 4  # You can change the value of x
n = 10  # Number of terms in the series

expansion = maclaurin_series_tan(x, n)
print(f"Maclaurin series of tan({x}) up to {n} terms: {expansion}")
