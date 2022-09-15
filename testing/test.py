from ast import Num
import unittest
from main import Doing_stuff


class TestDoing_stuff(unittest.TestCase):
    def setUp(self):
        print('about to test a class')

    def test_do_stuff(self):
        test_param = Doing_stuff()
        num = 10
        result = test_param.do_stuff(num)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = Doing_stuff()
        num = 'mike'
        result = test_param.do_stuff(num)
        self.assertIsInstance(result, ValueError)


unittest.main()
