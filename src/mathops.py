def multiply(a, b):
    # multiplies two numbers without type hinting
    result = 0
    for i in range(b):     # inefficient way to multiply
        result += a
    return result
