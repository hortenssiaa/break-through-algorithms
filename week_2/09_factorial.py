# Faccotial(N) = N * Factorial(N - 1)
# ...
# Faccotial(1) = 1

# 5 * 4 * 3 * 2 * facorial(1)
def factorial(n): # n == 1
    if n <= 1:     # factorial(1) == 1
        return 1
    return n * factorial(n - 1)


print(factorial(5))