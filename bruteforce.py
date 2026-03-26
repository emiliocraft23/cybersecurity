import itertools
import string
import time
import sys


def brute_force(target, alphabet=string.ascii_lowercase, max_len=None):
    attempts = 0
    start = time.perf_counter()
    if max_len is None:
        max_len = len(target)

    for length in range(1, max_len + 1):
        for comb in itertools.product(alphabet, repeat=length):
            attempts += 1
            s = ''.join(comb)
            if s == target:
                return s, attempts, time.perf_counter() - start

    return None, attempts, time.perf_counter() - start


def main():
   
    target = 'gaming'
    alphabet = string.ascii_lowercase
    if len(sys.argv) > 1:
        target = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == 'digits':
        alphabet = string.digits

    found, attempts, elapsed = brute_force(target, alphabet)
    if found:
        print(f"Encontrada: {found}")
        print(f"Intentos: {attempts}")
        print(f"Tiempo: {elapsed:.6f} s")
    else:
        print("No encontrada")
        print(f"Intentos: {attempts}")
        print(f"Tiempo: {elapsed:.6f} s")


if __name__ == '__main__':
    main()