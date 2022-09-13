def reverse_sentence(sentence: str) -> str:
    return " ".join(map(reverse_word, sentence.split()))


def reverse_word(word: str) -> str:
    char_only = list(filter(str.isalpha, word))
    return "".join([char if not char.isalpha() else char_only.pop() for char in word])


if __name__ == "__main__":
    cases = [("abcd efgh!", "dcba hgfe!"), ("a1bcd efg!h", "d1cba hgf!e"), ("", "")]

    for text, reversed_text in cases:
        assert reverse_sentence(text) == reversed_text
