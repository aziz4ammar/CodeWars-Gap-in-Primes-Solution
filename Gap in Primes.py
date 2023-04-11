def is_prime(n):
    """
    Function to check if a given number is prime.
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def gap(g, m, n):
    """
    Function to find the first pair of prime numbers with a gap of g between them.
    """
    prev_prime = None
    for i in range(m, n + 1):
        if is_prime(i):
            if prev_prime is not None and i - prev_prime == g:
                return [prev_prime, i]
            prev_prime = i
    return None
