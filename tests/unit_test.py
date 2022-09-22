import unittest

import anagrams


class TestStringMethods(unittest.TestCase):
    def test_compare_sentence(self):
        """check for execution correctness"""
        cases = [
            ("Python is love", "nohtyP si evol"),
            ("Foxminded is cool", "dednimxoF si looc"),
            ("AAaa2 AA", "aaAA2 AA"),
            ("Red nails ", "deR slian"),
        ]
        for text, reversed_tsxt in cases:
            with self.subTest(text):
                self.assertEqual(anagrams.reverse_sentence(text), reversed_tsxt)

    def test_check_for_wrong_type_sentence(self):
        """check for wrong type"""
        list_example_for_mistake = [
            123,
            [1, 2, 3, 4],
            {"Saasha": "ahsaS", "python123": "nohtyp123"},
        ]

        for text, example in enumerate(list_example_for_mistake):
            with self.subTest(text):
                with self.assertRaises(TypeError) as error:
                    anagrams.reverse_sentence(example)
                assert str(error.exception) == "Argument must be a string"

    def test_compare_word(self):
        """check for execution correctness"""
        cases = [
            ("Python", "nohtyP"),
            ("Python", "nohtyP"),
            ("AAaa2", "aaAA2"),
            ("Sasha123", "ahsaS123"),
        ]
        for text, reversed_tsxt in cases:

            with self.subTest(text):
                self.assertEqual(anagrams.reverse_word(text), reversed_tsxt)

    def test_check_for_wrong_type_word(self):
        """check for wrong argument type in word"""
        list_example_for_mistake = [
            123,
            [1, 2, 3, 4],
            {"Saasha": "ahsaS", "python123": "nohtyp123"},
        ]
        for text, example in enumerate(list_example_for_mistake):
            with self.subTest(text):
                with self.assertRaises(TypeError) as error:
                    anagrams.reverse_word(example)
                assert str(error.exception) == "Argument must be a string"
