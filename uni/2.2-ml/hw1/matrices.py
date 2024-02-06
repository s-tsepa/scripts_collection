from dataclasses import dataclass
from typing import Sequence
import numpy as np

Matrix = Sequence[Sequence]

COEF_LABEL_ROUND_SIGNS = 3


def matmul(a: Matrix, b: Matrix):
    dim_a_0 = len(a)
    dim_a_1 = len(a[0])

    print(f'a\'s shape: ({dim_a_0, dim_a_1})')

    dim_b_0 = len(b)
    dim_b_1 = len(b[0])

    print(f'a\'s shape: ({dim_b_0, dim_b_1})')

    if dim_a_1 != dim_b_0:
        raise Exception(f'Dimensions does not fit')

    row_len = dim_a_1

    c = [[0 for _ in range(dim_b_1)] for _ in range(dim_a_0)]

    for i in range(dim_a_0):
        for j in range(dim_b_1):
            x_ij = sum([a[i][k] * b[k][j] for k in range(row_len)])
            c[i][j] = x_ij

    return c


@dataclass
class Curve:
    xs: Sequence[float]
    ys: Sequence[float]
    label: str

    def __iter__(self):
        return iter([self.xs, self.ys, self.label])


def curve_label(coeffs: list[float]) -> str:
    s = ''
    pow = 0

    filtered_coeffs = list(filter(
        lambda x: x != 0,
        map(
            lambda x: round(x, COEF_LABEL_ROUND_SIGNS),
            reversed(coeffs)
        )
    ))

    for c in filtered_coeffs:
        if c != 0:
            s_coef = f'+ {c}' if c > 0 and len(filtered_coeffs) != 1 else f'{c}'
            s_x = '' if pow == 0 else 'x' if pow == 1 else f'x^{pow}'
            s = f'{s_coef}{s_x} ' + s

        pow += 1
    return 'y = ' + s


def curve_value_at(coeffs: list[float], x) -> float:
    res = 0
    pow = 0
    for c in reversed(coeffs):
        res += c * x ** pow
        pow += 1

    return res


def get_curve(coeffs: list[float], x_lim=None, step=1) -> Curve:
    # f = lambda x: a * x ** 2 + b * x + c

    # x_left, x_right = x_lim
    # x_coords = np.arange(x_left, x_right, (x_right - x_left) / count).reshape(-1, 1)
    # x_coords = list(x_coords.transpose()[0])

    xs = list(np.arange(x_lim[0], x_lim[1], step))
    ys = [curve_value_at(coeffs, x) for x in xs]

    return Curve(xs, ys, curve_label(coeffs))


def nullspace(a: Matrix):
    """
    Ax = 0

    Find such x that fits to equation
    """
    pass


def ax_equals_b(a: Matrix, b: Matrix):
    """
    Ax = b
    Solution x = x_p + x_n

    Find such x that fits to equation
    """
    pass


if __name__ == "__main__":
    a = np.array([
        [1, 2],
        [3, 4],
        [5, 6],
        [10, -1]
    ])

    b = np.array([
        [1],
        [2],
    ])

    my = matmul(a, b)
    his = np.matmul(a, b)

    print(np.array(my), my == list(his))
