def palindromeCheck(arrayList):
    backwardArray = arrayList[::-1]
    if backwardArray == arrayList:
        print("It is a palindrome")
    else:
        print("Not a palindrome")

arrayInput=input(str("Enter array(use commas and no spaces): "))
arrayList = arrayInput.split(",")
print(arrayList)
palindrome = palindromeCheck(arrayList)

    
