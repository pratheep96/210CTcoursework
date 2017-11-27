P1 = input("Enter the coefficients of the first polynomial(with commas): ")
P2 = input("Enter the coefficients of the second polynomial(with commas): ")
P1 = [int(x) for x in P1.split(',') if x]
P2 = [int(x) for x in P2.split(',') if x]
count1 = len(P1)-1
count2 = len(P2)-1
count = 0
List1 = []
List2 = []
while count1 > -1:
    result = count1 * P1[count]
    List1.append(result)
    count1 = count1 - 1
    count = count + 1
    
count = 0

while count2 > -1:
    result = count2 * P2[count]
    List2.append(result)
    count2 = count2 - 1
    count = count + 1

print(List1)
print(List2)


