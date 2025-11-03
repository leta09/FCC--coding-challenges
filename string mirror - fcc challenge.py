import re
def is_mirror(str1, str2):

    return re.sub(r'[^a-zA-Z]', '', str1)[::-1] == re.sub(r'[^a-zA-Z]', '', str2)

print(is_mirror("Hello World", "dlroW olleH"))

print(is_mirror("RaceCar", "RaceCar"))

print(is_mirror("Hello World", "dlroW-olleH") )



