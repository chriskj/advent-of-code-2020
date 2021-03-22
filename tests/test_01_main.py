import shutil
shutil.sys.path.append(r'../01/')

import unittest

import main as m


class Test01(unittest.TestCase):
    
    def test_import_amounts(self):
        amounts = m.import_amounts()
        assert isinstance(amounts, list)
        for amount in amounts:
            assert isinstance(amount, int)

    def test_two_sums_problem(self):
        amounts = list(range(1, 11))
        target = 10
        solutions = m.two_sums_problem(amounts, target)
        assert isinstance(solutions, list)
        for solution in solutions:
            assert isinstance(solution, list)
            assert sum(solution) == target

    def test_three_sums_problem(self):
        amounts = list(range(1, 11))
        target = 10
        solutions = m.three_sums_problem(amounts, target)
        assert isinstance(solutions, list)
        for solution in solutions:
            assert isinstance(solution, list)
            assert sum(solution) == target


if __name__ == '__main__':
    unittest.main()
