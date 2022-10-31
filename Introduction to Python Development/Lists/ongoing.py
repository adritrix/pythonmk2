from os import remove


my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list)
print("----------------------------------------")
# print(my_list[1])
# print(len(my_list))

# print(my_list[len(my_list)-1])

print(my_list[0:11:1])
print(my_list[11:0:-1])

my_list.append("pedro")

print(my_list)

my_list.remove("pedro")

print(my_list)

my_list.pop(0)
my_list.pop()
print(my_list)

my_list = [1,2,3,4,5,6,7,8,9,10]

my_list.insert(4,"pedro")

print(my_list)

my_listv2 = [1,2,3]

a,b,c = my_listv2

print(a,b,c)