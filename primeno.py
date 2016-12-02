def prime_num(number):
    # The list of prime numbers
    primenumbers = []
    isdivisible = True
    if not isinstance(number, int):
        return "only intergers are allowed"

    if number < 0:
        return "Negative numbers not allowed"
    else:
        for i in range(2, number + 1):
            isdivisible = True
            for j in range(2, i):
                if i % j == 0:  # if i is divisible by j
                    isdivisible = False
            if isdivisible:
                primenumbers.append(i)
    return primenumbers


print(prime_num(10))
