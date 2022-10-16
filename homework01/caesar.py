import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    if shift < 0:
        shift = 26 + shift
    a = []
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            a.append(ord(plaintext[i]))
        else:
            a.append(ord(plaintext[i]) - shift)
    for i in range(len(a)):
        temp = a[i] + shift
        if plaintext[i].isalpha():
            if a[i] >= ord("a") and a[i] <= ord("z"):
                # Маленькие буквы
                if temp > ord("z"):
                    a[i] = shift - (ord("z") - a[i]) + ord("a") - 1
                else:
                    a[i] = a[i] + shift
            else:
                # Большие буквы
                if temp > ord("Z"):
                    a[i] = shift - (ord("Z") - a[i]) + ord("A") - 1
                else:
                    a[i] = a[i] + shift
        else:
            a[i] = a[i] + shift
    for i in range(len(a)):
        ciphertext += chr(a[i])
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    return encrypt_caesar(ciphertext, -shift)


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
