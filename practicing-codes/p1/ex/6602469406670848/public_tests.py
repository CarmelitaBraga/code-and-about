import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
remove_trios = getattr(undertest, 'remove_trios', None)

class PublicTests(unittest.TestCase):

    def test_example(self):
        l = [1, 1, 2, 1]
        remove_trios(l)
        assert l == [2]

    def test_exemplo2(self):
        l = [1, 2, 1, 2, 1, 1]
        remove_trios(l)
        assert l == [1, 2, 1, 2, 1, 1]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
