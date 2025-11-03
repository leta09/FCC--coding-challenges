def get_words(paragraph):
    p = []
    for i in paragraph.split():
        if "," in i:
            p.append(i.replace(",", ""))
        elif "." in i:
            p.append(i.replace(".", ""))
        elif "!" in i:
            p.append(i.replace("!", ""))
        else:
            p.append(i.lower())

    p = [ i.lower() for i in p]
    d = { word : p.count(word)  for word in p}

    d_keys = [ t[0] for t in sorted(d.items(), key=lambda item: item[1], reverse=True)] 

    return d_keys[:3]


print(get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding"))
print(get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!"))
print(get_words("I like coding. I like testing. I love debugging!"))

