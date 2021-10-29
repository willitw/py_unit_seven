import unittest
import strings_one


class MyTestCase(unittest.TestCase):

    def test_half_slice_even(self):
        self.assertEqual("utercomp", strings_one.half_slice("computer"))
        self.assertEqual("ih", strings_one.half_slice("hi"))


    def test_half_slice_odd(self):
        self.assertEqual("erflybutt", strings_one.half_slice("butterfly"))
        self.assertEqual("anc", strings_one.half_slice("can"))

if __name__ == '__main__':
    unittest.main()
