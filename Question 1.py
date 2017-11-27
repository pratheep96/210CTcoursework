firstString=input("Enter the first word: ")
secondString=input("Enter the second word: ")
firstWord=list(firstString)
secondWord=list(secondString)
finalWord=[]
count = 0
if len(firstString)<len(secondString):
    while count < len(secondString):
        if count == len(firstString):
            while count < len(secondString):
                finalWord.append(secondWord[count])
                count = count + 1
        elif count < len(firstString) and count < len(secondString):
            finalWord.append(firstWord[count])
            finalWord.append(secondWord[count])
        count = count + 1
elif len(secondString) < len(firstString):
    while count < len(firstString):
        if count == len(secondString):
            while count < len(firstString):
                finalWord.append(firstWord[count])
                count = count + 1
        elif count < len(firstString) and count < len(secondString):
            finalWord.append(firstWord[count])
            finalWord.append(secondWord[count])
        count = count + 1
else:
    while count < len(firstString):
        finalWord.append(firstWord[count])
        finalWord.append(secondWord[count])
        count = count + 1
        
finalString=''.join(finalWord)
print(finalString)
