#Function to check for palindrome
def palindromeCheck(arrayList):
    backwardArray = arrayList[::-1]
    if backwardArray == arrayList:
        print("It is a palindrome")
    else:
        print("Not a palindrome")

#Asks for user input
arrayInput=input(str("Enter array(use commas and no spaces): "))
arrayList = arrayInput.split(",")
#Prints result
print(arrayList)
palindrome = palindromeCheck(arrayList)

    
