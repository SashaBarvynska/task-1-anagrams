def reverse_sentence(sentence: str) -> str:

    return " ".join(map(lambda x: reverse_word(x), sentence.split()))


def reverse_word(word: str) -> str:

    char_only = list(filter(lambda x: x.isalpha(), word))
    str_star = "".join([char if char.isalpha() == False else "*" for char in word])
    return "".join([char_only.pop() if char == "*" else char for char in str_star])


if __name__ == "__main__":
    cases = [("abcd efgh", "dcba hgfe"), ("a1bcd efg!h", "d1cba hgf!e"), ("", "")]

    for text, reversed_text in cases:
        assert reverse_sentence(text) == reversed_text
