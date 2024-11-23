import random


class TestCase:
    def __init__(self, n_limits, ai_limits):
        self.n_limits, self.ai_limits = n_limits, ai_limits

    def gen_case_common(self):
        n = random.randint(*self.n_limits)
        nums = [random.randint(*self.ai_limits) for _ in range(n)]
        return n, nums


def get_test_string(n, nums):
    return str(n) + '\n' + ' '.join(str(num) for num in nums)


TEST_CASES = [(TestCase((1, 10), (1, 10)), 5),
              (TestCase((10, 100), (1, 100)), 10),
              (TestCase((10 ** 2, 10 ** 3), (1, 10 ** 3)), 10),
              (TestCase((10 ** 3, 10 ** 4), (10 ** 2, 10 ** 3)), 10),
              (TestCase((10 ** 4, 10 ** 5), (10 ** 3, 10 ** 5)), 10),
              (TestCase((10 ** 5 - 10 ** 4, 10 ** 5),
                        (10 ** 5 - 10 ** 4, 10 ** 5)), 3)]
