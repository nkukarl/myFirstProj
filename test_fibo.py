from unittest import TestCase


class TestFibo(TestCase):
    def test_fibo(self):
        from fibo import fibo_gen
        self.assertTrue(fibo_gen(1) == 1)
        self.assertTrue(fibo_gen(9) == 34)
        self.assertTrue(fibo_gen(5) == 5)
