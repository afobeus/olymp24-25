import random


class TestCase:
    def __init__(self, n_limits, ai_limits, bi_limits):
        self.n_limits = n_limits
        self.ai_limits = ai_limits
        self.bi_limits = bi_limits

    def gen_case_common(self):
        n = random.randint(*self.n_limits)
        if random.random() < 0.75:
            nums = [[random.randint(*self.ai_limits)] for _ in range(n)]
            for i in range(n):
                nums[i].append(random.randint(self.bi_limits[0], min(self.bi_limits[1], nums[i][0])))
        else:
            nums = [[random.randint(*self.ai_limits),
                     random.randint(*self.bi_limits)] for _ in range(n)]
        return n, nums


def get_test_string(n, nums):
    return str(n) + '\n' + '\n'.join(f"{elem[0]} {elem[1]}" for elem in nums)


TEST_CASES = [(TestCase((1, 10), (1, 10), (1, 10)), 5),
              (TestCase((10, 100), (1, 100), (1, 100)), 10),
              (TestCase((100, 10 ** 3), (1, 10 ** 3), (1, 10 ** 3)), 10),
              (TestCase((10 ** 3, 10 ** 5), (1, 10 ** 9), (1, 10 ** 9)), 20),
              (TestCase((10 ** 5 - 1000, 10 ** 5), (1, 10 ** 9), (1, 10 ** 9)), 3)]
