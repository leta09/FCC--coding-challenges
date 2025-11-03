def all_unique(s):

    ascii = [ord(letter) for letter in s]

    return sorted(ascii) == sorted(list(set(ascii)))

print(all_unique("abc"))
print(all_unique("freeCodeCamp"))
print(all_unique("aA"))


