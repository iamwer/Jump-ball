def translate(phrase):
    tranlsation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                tranlsation = tranlsation + "G"
            else:
                tranlsation = tranlsation + g
        else:
            tranlsation = tranlsation + letter
    return tranlsation

print(translate(input("Enter a phrase")))