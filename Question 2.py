initialNumber = int(input("Enter the number: "))
numberList = str(initialNumber)
numberList = list(numberList)
numberList = list(map(int, numberList))
count = 0
total = 0
while count < len(numberList):
    total = total + ((numberList[count])**3)
    count = count + 1

if total == initialNumber:
    print("Yes it is an Armstrong number")
else:
    print("No it is not an Armstrong number")
    
    
