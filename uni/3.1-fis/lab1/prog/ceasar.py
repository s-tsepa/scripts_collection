"""
Ceasar cipher implementation
"""

from dataclasses import dataclass


def shift_text(s: str, offset: int, alphabet_size: int = 26, base_chr = "a", shift_forward: bool = True) -> str:
    result = ''

    coeff = -1 if not shift_forward else 1
    for i in s:
        new_i_char = ord(base_chr) + ((ord(i) - ord(base_chr) + offset * coeff) % alphabet_size)
        result += chr(new_i_char)

    return result


def encrypt(s: str, offset: int, alphabet_size: int = 26, base_chr="a") -> str:
    return shift_text(s, offset, alphabet_size, base_chr, shift_forward=True)


def decrypt(s: str, offset: int, alphabet_size: int = 26, base_chr="a") -> str:
    return shift_text(s, offset, alphabet_size, base_chr, shift_forward=False)


if __name__ == "__main__":
    sample_text = input()

    offset_key = 1

    encrypted = encrypt(s=sample_text, offset=offset_key)
    print("Encrypted: ", encrypted)
    decrypted = decrypt(s=encrypted, offset=offset_key)
    print("Decrypted: ", decrypted)

    if sample_text == decrypted:
        print("ENCRYPTION & DECRYPTION is correct")
    else:
        print("ENCRYPTION & DECRYPTION is wrong!")
