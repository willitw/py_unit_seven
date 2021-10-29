import unittest
import strings_two


class MyTestCase(unittest.TestCase):
    def test_four_letters(self):
        phrase1 = "Only a life lived for others is a life worthwhile"
        phrase1_four = "#$%@ a #$%@ lived for others is a #$%@ worthwhile"
        phrase2 = "Never let the fear of striking out keep you from playing the game"
        phrase2_four = "Never let the #$%@ of striking out #$%@ you #$%@ playing the #$%@"
        self.assertEqual(phrase1_four, strings_two.four_letters(phrase1))
        self.assertEqual(phrase2_four, strings_two.four_letters(phrase2))

    def test_bubble_sort(self):
        names = ["David", "Halley", "Khalid", "Anthony", "Caleb", "Aden"]
        names_sorted = ["Aden", "Anthony", "Caleb", "David", "Halley", "Khalid"]
        phrase1 = "Only a life lived for others is a life worthwhile".split(" ")
        phrase1_sorted = ["a", "a", "for", "is", "life", "life", "lived", "Only", "others", "worthwhile"]
        self.assertEqual(names_sorted, strings_two.bubble_sort(names))
        self.assertEqual(phrase1_sorted, strings_two.bubble_sort(phrase1))



if __name__ == '__main__':
    unittest.main()
