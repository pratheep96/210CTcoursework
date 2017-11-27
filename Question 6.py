def linearSearch(numberInput, numberList):
    if numberList:
        if numberInput == numberList[0]:
            print("Found the number " + str(numberInput))
        else:
            numberList = numberList[1:]
            linearSearch(numberInput, numberList)
    else:
        print("Number not found")
    

numberInput = int(input("Enter number: "))
numberList = [4, 7, 20, 13, 17, 24, 32, 38, 43, 23, 12, 57, 14, 19, 70, 56, 2, 54, 34]
linearSearch(numberInput, numberList)
