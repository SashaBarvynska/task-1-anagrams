if __name__ ==  '__main__':
    cases = [("abcd efgh", "dcba hgfe"), ("a1bcd efg!h", "d1cba hgf!e"), ("", "")]
    
    def your_function(text):
        str_new = ""
        for word in text.split():
            str_new += reverse_word(word) + " "
        return str_new[:-1]
        
    def reverse_word(word):
        list_new = list(word)
        start_index = 0
        end_index = len(list_new) - 1
        while start_index < end_index:
            if not list_new[start_index].isalpha():
                start_index += 1
            elif not list_new[end_index].isalpha():
                end_index -= 1
            else:
                list_new[start_index], list_new[end_index] = list_new[end_index], list_new[start_index]
                start_index += 1
                end_index -= 1
        return ''.join(list_new)
    for text, reversed_text in cases:
        assert your_function(text) == reversed_text

   
