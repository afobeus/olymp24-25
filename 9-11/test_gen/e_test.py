import random


class TestCase:
    def __init__(self, n_limits, q_limits, nums_limits):
        self.n_limits, self.q_limits, self.nums_limits = n_limits, q_limits, nums_limits

    def gen_case_common(self):
        n = random.randint(*self.n_limits)
        nums = [random.randint(*self.nums_limits) for _ in range(n)]
        q = random.randint(*self.q_limits)
        requests = []
        for i in range(q):
            requests.append([random.randint(1, 2)])
            if requests[-1][0] == 1:
                requests[-1].append(random.randint(0, n - 1))
                requests[-1].append(random.randint(requests[-1][1], n - 1))
            else:
                requests[-1].extend([random.randint(0, n - 1), random.randint(*self.nums_limits)])
        return n, nums, q, requests


def get_test_string(n, nums, q, requests):
    return str(n) + '\n' + ' '.join(str(elem) for elem in nums) + '\n' + str(q) + '\n' + \
        '\n'.join(f"{elem[0]} {elem[1]} {elem[2]}" for elem in requests)


TEST_CASES = [(TestCase((1, 10), (1, 10), (-10, 10)), 5),
              (TestCase((10, 10 ** 2), (10, 10 ** 2), (-100, 100)), 10),
              (TestCase((10 ** 2, 10 ** 4), (10 ** 2, 10 ** 4), (-10 ** 5, 10 ** 5)), 10),
              (TestCase((10 ** 4, 10 ** 5), (10 ** 4, 10 ** 5), (-10 ** 9, 10 ** 9)), 10),
              (TestCase((10 ** 5, 10 ** 6), (10 ** 5, 10 ** 6), (-10 ** 9, 10 ** 9)), 5),
              (TestCase((10 ** 6 - 10 ** 5, 10 ** 6), (10 ** 6 - 10 ** 5, 10 ** 6), (-10 ** 9, 10 ** 9)), 2)]
