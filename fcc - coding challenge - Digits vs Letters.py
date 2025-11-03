
def digits_or_letters(s):
    letters = 0
    digits = 0
    for letter in s:
        if letter.isalpha():
            letters += 1
        if letter.isnumeric():
            digits += 1
    
    if letters > digits:
        return "letters"
    elif digits > letters:
        return "digits"
    else:
        return "tie"


