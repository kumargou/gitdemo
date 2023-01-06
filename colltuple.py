my_tuple=("apple","oranges","banana")
print(my_tuple)
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[0:3])

for val in my_tuple:
    print(val)
#my_tuple[3]="cherry"
#del my_tuple[2]

print(len(my_tuple))

mytp2=("rose",(1,2,3),["india","japan","usa"])
print(mytp2)
print(mytp2[1])
print(len(mytp2[1]))
print(mytp2[1][1])
print(mytp2[2][1])
mytp2[2][1] = "UK"
print(mytp2[2][1])

print("banana" in my_tuple)
print("india" in mytp2[2])
print("usa" in my_tuple)

mytp3=("laptop","tv","laptop") #allows duplicates
print(mytp3)

mytp=() #empty tuple
print(mytp)
ptint("Develop dev2")
