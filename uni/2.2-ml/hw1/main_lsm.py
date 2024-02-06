import numpy as np

from typing import Sequence
from matplotlib import pyplot as plt

from matrices import get_curve
from lsm import lsm_matrix, lsm_analytical_line

MAX_DEGREE = 1

# data = pd.read_csv('task1_data.csv')
#
# x_train = data.T.values[0]
# y_train = data.T.values[1]
# x_test = data.T.values[2]
# y_test = data.T.values[3]

Points = tuple[Sequence[float], Sequence[float]]


def correlated_data() -> Points:
    xx = np.array([-0.51, 51.2])
    yy = np.array([0.33, 51.6])
    means = [xx.mean(), yy.mean()]
    stds = [xx.std() / 3, yy.std() / 3]
    corr = 0.8  # correlation
    covs = [[stds[0] ** 2, stds[0] * stds[1] * corr],
            [stds[0] * stds[1] * corr, stds[1] ** 2]]

    m = np.random.multivariate_normal(means, covs, 1000).T
    xs, ys = m
    xs = xs.reshape(-1, 1)
    ys = ys.reshape(-1, 1)

    return xs, ys


def my_points() -> Points:
    points = np.array([
        # [190.2, 214],
        # [248.4, 282],
        # [263.8, 300],
        # [314.2, 359]

        [214, 190.2],
        [282, 248.4],
        [300, 263.8],
        [359, 314.2]
    ])

    xs, ys = np.split(points, 2, axis=1)
    return xs, ys


if __name__ == "__main__":
    border = 500
    plt.xlim(0, border)
    plt.ylim(0, border)

    n = 500
    np.random.seed(10)

    # xs, ys = correlated_data()
    xs, ys = my_points()

    plt.scatter(xs, ys)

    coeffs = lsm_matrix(xs, ys, max_degree=MAX_DEGREE)

    # coeffs2 = lsm_analytical_line(xs, ys)
    # delta = 10 ** -6
    # coeffs_diff = np.array(coeffs) - np.array(coeffs2)
    # assert (coeffs_diff < delta).all()

    xs_curve, ys_curve, label_curve = get_curve(coeffs, [-border, border], step=0.5)

    plt.plot(
        xs_curve, ys_curve,
        label=label_curve,
        linewidth="3",
        # marker="o",
        # markersize=4,
        color="green"
    )

    plt.legend()
    plt.show()
