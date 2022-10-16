def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""

    for i in range(len(plaintext)):
        l = ord(plaintext[i])
        shift = ord(keyword[i % len(keyword)])  # смещене

        k = ord(keyword[i % len(keyword)])  # порядковый номер, A-Z, a-z
        if k >= ord("a") and k <= ord("z"):
            shift -= ord("a")
        else:
            shift -= ord("A")

        if plaintext[i].isalpha():
            if l >= ord("a") and l <= ord("z"):
                temp = l + shift
                if temp > ord("z"):
                    ciphertext += chr(shift - (ord("z") - l) + ord("a") - 1)
                else:
                    ciphertext += chr(temp)
            else:
                temp = l + shift
                if temp > ord("Z"):
                    ciphertext += chr(shift - (ord("Z") - l) + ord("A") - 1)
                else:
                    ciphertext += chr(temp)
        else:
            ciphertext += plaintext[i]

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    ciphertexttext = ""

    for i in range(len(ciphertext)):
        l = ord(ciphertext[i])
        shift = ord(keyword[i % len(keyword)])

        k = ord(keyword[i % len(keyword)])
        if k >= ord("a") and k <= ord("z"):
            shift -= ord("a")
        else:
            shift -= ord("A")

        shift = 26 - shift

        if ciphertext[i].isalpha():
            if l >= ord("a") and l <= ord("z"):
                temp = l + shift
                if temp > ord("z"):
                    ciphertexttext += chr(shift - (ord("z") - l) + ord("a") - 1)
                else:
                    ciphertexttext += chr(temp)
            else:
                temp = l + shift
                if temp > ord("Z"):
                    ciphertexttext += chr(shift - (ord("Z") - l) + ord("A") - 1)
                else:
                    ciphertexttext += chr(temp)
        else:
            ciphertexttext += ciphertext[i]

    return ciphertexttext
