"""
### Compare the Triplets
#
a = []
b = []
c = list(range(0,2))
z = 3
a1, a2, a3 = [int(x) for x in input().split()]          #input kesamping
a.append(a1)        #masukin var ke array
a.append(a2)
a.append(a3)
b1, b2, b3 = [int(x) for x in input().split()]
b.append(b1)
b.append(b2)
b.append(b3)
nilaiA = 0
nilaiB = 0
i = 0
for g in range (z):
    if a[i] > b[i]:
        nilaiA = nilaiA + 1
    elif a[i] < b[i]:
        nilaiB = nilaiB + 1
    i = i + 1

c[0] = nilaiA;
c[1] = nilaiB;

print(c[0],c[1])

############################

a = []
b = []
c = list(range(0,2))
z = 3
for i in range (z):
    temp = int(input())
    a.append(temp)
for i in range (z):
    temp = int(input())
    b.append(temp)
i = 0
nilaiA = 0
nilaiB = 0
for g in range (z):
    if a[i] > b[i]:
        nilaiA = nilaiA + 1
    elif a[i] < b[i]:
        nilaiB = nilaiB + 1
    i = i + 1

c[0] = nilaiA;
c[1] = nilaiB;

print(c)

### Diagonal Difference

n=int(input())
arr = []

for i in range (n):
   arr.append([int(y) for y in input().split()])

i = 0
j = 0
sum1 = 0
for z in range (n):
    sum1 = sum1 + arr[i][j]
    i = i + 1
    j = j + 1

i = 0
j = n-1
sum2 = 0
for z in range (n):
    sum2 = sum2 + arr[i][j]
    j = j - 1
    i = i + 1

print(abs(sum1-sum2))

####################

### Staircase

n = int(input())
k = n-1
for i in range(n):
    for j in range(k): 
            print(end=" ")      #untuk spasi
    k = k - 1
    for j in range(i+1): 
        print('#',end="")
    print("\r")                 #new line


#######################
"""

print("Mini-Max Sum\r")
arr = []

b1, b2, b3, b4 = [int(x) for x in input().split()]
arr.append(b1)
arr.append(b2)
arr.append(b3)
arr.append(b4)

print(arr)
print(sum(arr))
