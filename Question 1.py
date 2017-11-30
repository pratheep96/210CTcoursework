#This asks for the user to input
firstString=input("Enter the first word: ") 
secondString=input("Enter the second word: ") 
#This converts the user input into list
firstWord=list(firstString)                 
secondWord=list(secondString)
#This sets up a blank array
finalWord=[]                                 
count = 0

#Each loop places each letter one after the other depending on which string is longer
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

#This joins the letters together        
finalString=''.join(finalWord)
print(finalString)
