def reverse_sentence(sentence: str) -> str:

    if not isinstance(sentence, str):
        raise TypeError("Argument must be a string")
    return " ".join(map(reverse_word, sentence.split()))


def reverse_word(word: str) -> str:

    if not isinstance(word, str):
        raise TypeError("Argument must be a string")
    char_only = list(filter(str.isalpha, word))
    return "".join([char if not char.isalpha() else char_only.pop() for char in word])
