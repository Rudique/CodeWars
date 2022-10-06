def fibonacci(n):
    try:
        fibonacci.array
    except:
        fibonacci.array = {1: 1, 2: 1}
    try:
        result = fibonacci.array[n]
    except:
        result = fibonacci(n-2) + fibonacci(n - 1)
        fibonacci.array[n] = result
    return result

print(fibonacci(50))
