import unittest
import assignment_seven


class MyTestCase(unittest.TestCase):
    def test_encode(self):
        self.assertEqual("sbwkrq", assignment_seven.encode("python", 3))


if __name__ == '__main__':
    unittest.main()
