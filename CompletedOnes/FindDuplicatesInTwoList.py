

list1 = [10,20,30,40,50]
list2 = [10,20,30,40,50,60]

seen = list(set(list1)) - set(list2)
print(seen)