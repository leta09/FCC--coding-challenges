
def get_longest_word(sentence):
    word_list = sentence.replace(".", "").split()
    lengths = [len(word) for word in word_list]

    max_len = max(lengths)

    for i in range(len(word_list)):
        if lengths[i] == max_len:
            return word_list[i]




print(get_longest_word("This sentence has multiple long words."))
print(get_longest_word("Coding challenges are fun and educational."))
print(get_longest_word("coding is fun"))


