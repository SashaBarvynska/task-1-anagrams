def reverse_sentence(sentence="") -> str:
    if sentence:
        if type(sentence) == str:
            return " ".join(map(reverse_word, sentence.split()))
        raise TypeError("String must be string...Try again")
    raise SyntaxError("String must not be empty...Try again")


def reverse_word(word: str) -> str:

    char_only = list(filter(str.isalpha, word))
    return "".join([char if not char.isalpha() else char_only.pop() for char in word])
