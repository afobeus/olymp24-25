import random


class TestCase:
    def __init__(self, n_limits):
        self.n_limits = n_limits

    def gen_case_common(self):
        n = random.randint(*self.n_limits)
        return n,


def get_test_string(n):
    return str(n)


TEST_CASES = [(TestCase((1, 10)), 5),
              (TestCase((-10, 0)), 1),
              (TestCase((10, 10 ** 3)), 10),
              (TestCase((-10 ** 3, 0)), 1),
              (TestCase((10 ** 3, 10 ** 9)), 10),
              (TestCase((-10 ** 9, 0)), 1),
              (TestCase((10 ** 9, 10 ** 18)), 10),
              (TestCase((-10 ** 18, 0)), 1),
              (TestCase((10 ** 18 - 10 ** 17, 10 ** 18)), 3),
              (TestCase((-10 ** 18, 0)), 1)]
