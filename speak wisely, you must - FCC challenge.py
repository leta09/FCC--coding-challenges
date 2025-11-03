** start of main.py **

def wise_speak(sentence):
    list_res = []
    last_char = sentence[-1]
    list_sentence = sentence[:len(sentence)-1].split()
    for word in list_sentence:
        if word == "have" or word == "must" or word == "are" or word =="will" or word == "can":
            ind = list_sentence.index(word) + 1
    
    list_res.append(list_sentence[ind]) 
    list_res += list_sentence[ind + 1:]
    sen_res = " ".join(list_res) + ", "
    sen_res += " ".join(list_sentence[:ind])
    sen_res += last_char


    return sen_res.lower().capitalize()

print(wise_speak("Do you think you will complete this?"))

** end of main.py **

