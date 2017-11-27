def mirrorString(string):
    return ' '.join(word[::-1] for word in string.split())

string = str(input("Enter a sentence: "))
mirrorSentence = mirrorString(string)
print(mirrorSentence)
