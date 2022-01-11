from numpy import gcd
from random import randint


# Função que calcula os valores das chaves de acordo as regras da
# Criptografia RSA
def generate() -> dict:

    # Calcular números primos
    prime_numbers = []
    for i in range(32, 317):
        if all(i % j != 0 for j in range(2, i)):
            prime_numbers.append(i)
    p = prime_numbers[randint(0, len(prime_numbers) - 1)]
    q = prime_numbers[randint(0, len(prime_numbers) - 1)]

    # Calcular n
    n = p * q

    # Calcular Phi(n)
    phi_n = (p - 1) * (q - 1)

    # Calcular e
    e = []
    for i in range(1000, 100000):
        if gcd(i, phi_n) == 1:
            e.append(i)
    e = e[randint(0, len(e) - 1)]

    # Calcular d
    d = []
    for i in range(1000, 100000):
        if (i * e) % phi_n == 1:
            d.append(i)
    d = d[randint(0, len(d) - 1)]

    # Retorno:
    # - Min caracteres: 4
    # - Max caracteres: 5

    return {
        "chave_n": n,
        "chave_e": e,
        "chave_d": d,
    }
