import unittest
import anagrams


class TestStringMethods(unittest.TestCase):
    def test_compere(self):
        with self.subTest():
            self.assertEqual(anagrams.reverse_sentence("Sasha"), "ahsaS")

    def test_check_for_wrong_type(self):
        # check for wrong type
        with self.assertRaises(TypeError) as error:
            anagrams.reverse_sentence(123)
        self.assertEqual(error.exception.args[0], "String must be string...Try again")

    def test_check_without_parameter(self):
        # check without parameter
        with self.assertRaises(SyntaxError) as error:
            anagrams.reverse_sentence()
        self.assertEqual(
            error.exception.args[0], "String must not be empty...Try again"
        )


if __name__ == "__main__":
    unittest.main()
