import random


class TestCase:
    def __init__(self, n_limits, m_limits):
        self.n_limits = n_limits
        self.m_limits = m_limits

    def gen_case_common(self):
        n = random.randint(*self.n_limits)
        k = random.randint(1, n)
        m = random.randint(*self.m_limits)
        nums = list(range(10, 100))
        random.shuffle(nums)
        ms = nums[:m]
        k_indexes = random.sample(list(range(n)), k)
        nums = list(range(10))
        ks = [[k_indexes[i], random.randint(1, 9)] for i in range(len(k_indexes))]
        for i in range(k):
            random.shuffle(nums)
            ks[i].extend(nums[:ks[i][-1]])
        return n, m, k, ms, ks


def get_test_string(n, m, k, ms, ks):
    return f"{n} {m} {k}" + '\n' + ' '.join(str(elem) for elem in ms) + '\n' +\
        '\n'.join(' '.join(str(elem) for elem in ks[i]) for i in range(len(ks)))


TEST_CASES = [(TestCase((1, 10), (1, 10)), 10),
              (TestCase((10, 100), (1, 10)), 10),
              (TestCase((100, 10 ** 3), (10, 89)), 10),
              (TestCase((10 ** 3, 10 ** 5), (10, 89)), 10),
              (TestCase((10 ** 5 - 1000, 10 ** 5), (80, 89)), 3)]
