import random


class TestCase:
    def __init__(self, t_limits, n_limits):
        self.t_limits = t_limits
        self.n_limits = n_limits

    def gen_case_common(self):
        t = random.randint(*self.t_limits)
        numbers = [random.randint(*self.n_limits) for _ in range(t)]
        return t, numbers


def get_test_string(t, numbers):
    return str(t) + '\n' + ' '.join(str(elem) for elem in numbers)


TEST_CASES = [(TestCase((1, 10), (1, 10)), 3),
              (TestCase((5, 10), (10 ** 2, 10 ** 3)), 5),
              (TestCase((10, 10 ** 2), (10 ** 2, 10 ** 3)), 5),
              (TestCase((10, 10 ** 2), (10 ** 3, 10 ** 6)), 5),
              (TestCase((1.5 * 10 ** 2, 10 ** 3), (1.5 * 10 ** 5, 10 ** 6)), 10)]
