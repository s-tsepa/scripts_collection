import functools
import math
import os
from typing import Literal


class DataInterface:
    @classmethod
    def from_bytes(cls, b: bytes):
        pass

    @classmethod
    def from_hex(cls, h: str):
        pass

    @classmethod
    def from_bin(cls, bin_str: str):
        pass

    @classmethod
    def from_int(cls, n: int):
        pass

    def to_bytes(self) -> bytes:
        pass

    def to_hex(self) -> str:
        pass

    def to_bin(self) -> str:
        pass


class BytesData(DataInterface):
    __bytes_arr = bytes()

    def __init__(self, b: bytes):
        self.__bytes_arr = b

    @classmethod
    def from_bytes(cls, b: bytes):
        return cls(b)

    @classmethod
    def from_hex(cls, h: str):
        """
        bytes <- hex
        """
        b = hex_to_bytes(h)
        return cls(b)

    @classmethod
    def from_bin(cls, bin_str: str):
        """
        bytes <- bin
        """
        b = bin_to_bytes(bin_str)
        return cls(b)

    @classmethod
    def from_int(cls, n: int):
        """
        bytes <- bin <- int
        """
        bin_str = int_to_bin(n)
        b = bin_to_bytes(bin_str)

        return cls(b)

    def to_bytes(self) -> bytes:
        return self.__bytes_arr

    def to_hex(self) -> str:
        """
        bytes -> hex
        """
        h = bytes_to_hex(self.__bytes_arr)
        return h

    def to_bin(self) -> str:
        """
        bytes -> bin
        """
        return bytes_to_bin(self.__bytes_arr)

    def to_int(self) -> int:
        """
        bytes -> bin -> int
        """
        bin_str = bytes_to_bin(self.__bytes_arr)
        n = bin_to_int(bin_str)
        return n

    def __str__(self) -> str:
        return str(self.to_bytes())

    def __repr__(self) -> str:
        return f"bytes: {self.to_bytes()}\nhex: {self.to_hex()}\nbin: {self.to_bin()}\nint: {self.to_int()}"



BLOCK_SIZE = 8
ENDIANNESS: Literal['big', 'little'] = 'big'


# ---- Utils funcs ----

def nearest_bigger(n, x):
    return math.ceil(n / x) * x
    # return n - (n % x) + x


def generator_to_list(func):
    @functools.wraps
    def inner(*args, **kwargs):
        return func(*args, **kwargs)

    return inner




def invert_bin(bin_str: str) -> str:
    return ''.join(['0' if i == '1' else '1' for i in bin_str])

# ---- Main funcs ----

def split_to_chunks(string,
                    block_size=BLOCK_SIZE,
                    fill_marginal_chunk=False,
                    is_fill_marginal_left=True) -> list:
    """
    split given string to chunks of block_size, additionally filling with zeros to right of left
    :param string: input string
    :param block_size: chunk size
    :param fill_marginal_chunk: whether to fill with zeros
    :param is_fill_marginal_left: on which side to fill
    :return: list of chunks as strings
    """

    def split_by(s, step) -> list:
        return [s[i:i + step] for i in range(0, len(s), step)]

    def fill_zeros(s, x, to_left=True) -> str:
        zero_pad = nearest_bigger(len(s), x)

        if to_left:
            return s.zfill(zero_pad)
        else:
            return s[::-1].zfill(zero_pad)[::-1]

    if fill_marginal_chunk:
        string = fill_zeros(
            string,
            block_size,
            to_left=is_fill_marginal_left
        )

    chunks_arr = split_by(string, block_size)
    return chunks_arr


def bytes_to_hex(b: bytes) -> str:
    # return binascii.hexlify(b)
    return b.hex()


def hex_to_bytes(hex_str: str) -> bytes:
    if len(hex_str) % 2 != 0:
        raise Exception

    @generator_to_list
    def my_func(hex_str_: str):
        hex_chunks: list[str] = split_to_chunks(
            hex_str_,
            block_size=2,
            fill_marginal_chunk=False
        )

        for i in hex_chunks:
            b = bytes.fromhex(i)
            yield b

    # return my_func(hex_str)
    # return binascii.unhexlify(hex_str)
    return bytes.fromhex(hex_str)


def int_to_bin(n: int, to_bytes_size=True):
    """
    zeros are added to the left
    """
    res = bin(n)[2:]

    if to_bytes_size:
        to_add_cnt = 8 - (len(res) % 8)
        if to_add_cnt == 8:
            to_add_cnt = 0

        res = to_add_cnt * "0" + res

    return res


def bin_to_int(b: str) -> int:
    b = b.replace(" ", "")
    return int(b, 2)


def bin_to_bytes(bin_str: str) -> bytes:
    if len(bin_str) % 8 != 0:
        raise Exception

    splitted_list: list[str] = split_to_chunks(bin_str)

    int_list: list[int] = list(map(bin_to_int, splitted_list))
    return bytes(int_list)


def bytes_to_bin(b: bytes) -> str:
    res = ""
    byte_int: int
    for byte_int in b:
        # byte.to_bytes(1, ENDIANNESS)

        bin_str: str = int_to_bin(byte_int)
        res += bin_str + " "

    return res


# ----


def _hex_to_int(h: str) -> int:
    return int(h, 16)


def _bytes_to_int(b: bytes) -> int:
    return int.from_bytes(b, ENDIANNESS)


def _int_to_bytes(n: int) -> bytes:
    raise NotImplementedError
    # return n.to_bytes()


# ---- ----

def random_bytes(n: int) -> bytes:
    """
    :param n: length (in bytes)
    :return: bytes array
    """
    res = os.urandom(n)

    assert len(res) == n
    return res


def random_bin(bytes_n: int) -> str:
    """
    Generates a random sequence of 0 and 1, stripped to given length (in bytes)
    :param bytes_n: bytes count
    :return: string of zeros and ones
    """

    rand_bytes = random_bytes(bytes_n)

    hd = BytesData.from_bytes(rand_bytes)
    bin_string = hd.to_bin()

    assert len(bin_string) == bytes_n * 8
    return bin_string


# if __name__ == "__main__":
    # while True:
    #     print(random_bin(bytes_n=10))
    # print(str(BytesData.from_hex('4d4e')
