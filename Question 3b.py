P1 = input("Enter the coefficients of the first polynomial(with commas): ")
P2 = input("Enter the coefficients of the second polynomial(with commas): ")
P1 = [int(x) for x in P1.split(',') if x]
P2 = [int(x) for x in P2.split(',') if x]
print(P1)
print(P2)
count1 = len(P1)-1
count2 = len(P2)-1
List1 = []
List2 = []
while count1 > -1:
    List1.append(count1)
    count1 = count1 - 1

while count2 > -1:
    List2.append(count2)
    count2 = count2 - 1
    
P1a = zip(P1, List1)
P2a = zip(P2, List2)
result = []
for i in P1a:
    for j in P2a:
        if i[1] + j[1] in result:
            result[i[1] + j[1]] += i[0] * j[0]
        else:
            result[i[1] + j[1]] = i[0] * j[0]

print(result)


