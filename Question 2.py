#Asks for user input
initialNumber = int(input("Enter the number: "))
#Converts numbers into string
numberList = str(initialNumber)
#Converts string into list
numberList = list(numberList)
#Seperates numbers into digits
numberList = list(map(int, numberList))
count = 0
total = 0
#Peforms armstrong number calculation for each digit
while count < len(numberList):
    total = total + ((numberList[count])**3)
    count = count + 1

if total == initialNumber:
    print("Yes it is an Armstrong number")
else:
    print("No it is not an Armstrong number")
    
    
