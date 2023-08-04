import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global idiff
        undertest = __import__(module)
        idiff = getattr(undertest, 'idiff', None)

    def test_exemplo(self):
        seq1 = [10, 20, 30, 40, 50, 60, 70]
        seq2 = [10, 20, 20, 40, 80]
        assert idiff(seq1, seq2) == [2, 4, 5, 6]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
