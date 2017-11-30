#Function to mirror each word in the sentence
def mirrorString(string):
    return ' '.join(word[::-1] for word in string.split())

#Asks user for input
string = str(input("Enter a sentence: "))
mirrorSentence = mirrorString(string)
#Prints the result  
print(mirrorSentence)
