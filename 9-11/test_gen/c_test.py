import random


class TestCase:
    def __init__(self, n_limits):
        self.n_limits = n_limits

    def gen_case_common(self):
        n = random.randint(*self.n_limits)
        letters = 'qwertyuiopasdfghjklzxcvbnm'
        string = ''.join(random.choice(letters) for _ in range(n))
        return n, string


def get_test_string(n, string):
    return str(n) + '\n' + string


TEST_CASES = [(TestCase((1, 10)), 5),
              (TestCase((10 ** 2, 10 ** 5)), 15),
              (TestCase((10 ** 5, 10 ** 6)), 20),
              (TestCase((10 ** 6, 10 ** 6)), 3)]
