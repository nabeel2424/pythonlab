count  = 0
while(count<5):
     print(count)
     count = count+1

print("Bye")

list1=[1, 2, 3, "Python"]
for i in list1:
    print(i)

fruits=["apple", "banana", "orange", "mango"]

for lol in range(len(fruits)):
    print(fruits[lol])


#nested loops

for i in range(1, 2):

    for j in range(1, 3):
        print("*")

print(str(0)*0)

range(0,0)


count=5
for i in range(10):
    print(str(i)*i)

    for j in range(0,i):
        count=count+1

#loop control

for i in range(10,50):
    print(i)
    if(i==30):
        break

""""for j in range(1,11):
    print(j)
    if(j==5):
        continue"""

for k in range(1,3):
    pass
print("loop ends here")
