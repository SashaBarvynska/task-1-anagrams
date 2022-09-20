import anagrams
import unittest


class TestStringMethods(unittest.TestCase):
    def test_compare(self):

        cases = [
            ("Python", "nohtyP"),
            ("Python", "nohtyP"),
            ("AAaa2", "aaAA2"),
            ("Sasha123", "ahsaS123"),
        ]
        i = 0
        for text, reversed_tsxt in cases:

            print(text, reversed_tsxt, "text, reversed_tsxt")
            with self.subTest(i=i):
                self.assertEqual(anagrams.reverse_sentence(text), reversed_tsxt)
            i += 1

    def test_check_for_wrong_type(self):
        """check for wrong type"""
        list_example_for_mistake = [
            123,
            [1, 2, 3, 4],
            {"Saasha": "ahsaS", "python123": "nohtyp123"},
        ]

        for i, example in enumerate(list_example_for_mistake):
            print(example, i, "example,i")
            with self.subTest(i=i):
                with self.assertRaises(TypeError) as error:
                    anagrams.reverse_sentence(example)
                assert error.exception.args[0] == "Argument must be a string"
