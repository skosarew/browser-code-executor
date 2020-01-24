# from django.test import TestCase

import unittest


class TestCaseForms(unittest.TestCase):
    def test_input_converter(self):
        input_text = "1 2 3\n4 5 6"
        input_gen = (x for x in input_text.splitlines())

        def input(*x):
            if x:
                print(x)
            res = next(input_gen)
            print(res)
            return res

        a, b, c = map(int, input("input abc").split())
        d, e, f = map(int, input().split())

        self.assertEqual((a, b, c), (1, 2, 3))
        self.assertEqual((d, e, f), (4, 5, 6))


if __name__ == '__main__':
    unittest.main()
