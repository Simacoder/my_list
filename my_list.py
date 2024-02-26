# wrking with list

my_list = []
for i in range(10,50,10):
    my_list.append(i)
print(my_list)
my_list.insert(1, 15)
print("new list")
print(my_list)
extend_list = [50,60,70]
my_list.extend(extend_list)
print("extended list")
print(my_list)
print("The removed last list")
my_list.pop(-1)
print(my_list)
print("now sort them list")
sorted(my_list)
print(my_list)
print("now finding value 30 n the list")
print(my_list[3])