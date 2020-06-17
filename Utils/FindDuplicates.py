# This Function finds number fo duplicates and counts

# We have two lists
# list1 = []
# list2 = []
#
# List one and list two has duplicates numbers that iterating multiple times, we need to find
# how many times it iterates in list1 and list2, and whatever is more the count we need to store
# in different list
#
# list1 = [1,1,2,2,3,3,4,4,4]
# list2 = [1,1,2,2,3,3,4,4,]
#
# the logic should be
#
# if list1 has number 1's two times, then take only two times number 1's from list2


list1 = [1, 1, 2, 2, 3, 3, 4, 4, 4]
new_dict = {}
count = []

for i in list1:
    new_dict[i] = list1.count(i)


for i in new_dict:
    count.append(new_dict[i])


print(new_dict)
print(count)



