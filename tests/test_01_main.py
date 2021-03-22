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


if __name__ == '__main__':
    unittest.main()
