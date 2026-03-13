def reverse_words(s):
    words_list = s.split(" ")
    revers_words = words_list[::-1]
    new_str = ""

    for word in revers_words:
        new_str = new_str + word + " "

    new_str.strip()

    return new_str

s = "the sky is blue"
s1 = "hello world"
print(reverse_words(s))
print(reverse_words(s1))