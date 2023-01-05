my_dict={
    "student" : "sevita",
    "std" : 2,
    "age" : 7
}
print(my_dict)
print(my_dict["student"])
print(my_dict.values())

for x in my_dict:
    print(x)
for x in my_dict:
    print(my_dict[x])
for x,y in my_dict.items():
    print(x,y)
my_dict["std"]=1
print(my_dict)
my_dict["result"]="PASS"
print(my_dict)

my_dict.pop("result")
print(my_dict)
my_dict.popitem()
print(my_dict)

del my_dict["student"]
print(my_dict)

my_dict.clear()
print(my_dict)

del my_dict
#print(my_dict)