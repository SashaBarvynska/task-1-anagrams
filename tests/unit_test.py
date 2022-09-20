import unittest
import anagrams


class TestStringMethods(unittest.TestCase):
    def test_compare(self):
        list_example = {"Sasha": "ahsaS", "python123": "nohtyp123"}
        with self.subTest():
            for example in list_example:
                self.assertEqual(
                    anagrams.reverse_sentence(example), list_example[example]
                )

    def test_check_for_wrong_type(self):
        """check for wrong type"""
        list_example_for_mistake = [
            123,
            [1, 2, 3, 4],
            {"Saasha": "ahsaS", "python123": "nohtyp123"},
        ]
        with self.assertRaises(TypeError) as error:
            for example in list_example_for_mistake:
                anagrams.reverse_sentence(example)
        self.assertEqual(error.exception.args[0], "Argument must be a string")
