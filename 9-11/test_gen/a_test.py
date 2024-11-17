import random


class TestCase:
    def __init__(self, n_limits, v_k_t_limits, r_limits):
        self.n_limits, self.v_k_t_limits, self.r_limits = n_limits, v_k_t_limits, r_limits

    def gen_case_common(self):
        n = random.randint(*self.n_limits)
        data = [[random.randint(*self.v_k_t_limits), random.randint(*self.v_k_t_limits),
                random.randint(*self.r_limits), random.randint(*self.v_k_t_limits),
                random.randint(*self.v_k_t_limits), random.randint(*self.r_limits),
                random.randint(*self.v_k_t_limits)] for _ in range(n)]
        return n, data


def get_test_string(n, data):
    return str(n) + '\n' + '\n'.join(' '.join(str(elem) for elem in data[i]) for i in range(len(data)))


TEST_CASES = [(TestCase((1, 10), (1, 10), (0, 10)), 5),
              (TestCase((1, 10 ** 3), (1, 10 ** 3), (0, 10 ** 3)), 10),
              (TestCase((1, 10 ** 6), (1, 10 ** 9), (0, 10 ** 9)), 40)]

