# This Function finds number fo duplicates and counts

# We have two lists
# list1 = []
# list2 = []
#
# List one and list two has duplicates numbers that iterating multiple times, we need to find
# how many times it iterates in list1 and list2, and whatever is more the count we need to store
# in different list
#
# list1 = 1, 1, 2, 2, 3, 3, 4, 4, 4]
# list2 = 1, 1, 2, 2, 3, 3, 4, 4]
#
# the logic should be
#
# if list1 has number 1's two times, then take only two times number 1's from list2

#i do have count now, i need to match count with list2, to do that i need to find coun of each element in the loop

list2 = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4]

list1 = [1, 1, 2, 2, 3, 3, 4, 4]
new_dict = {}
count = []

for i in list1:
    new_dict[i] = list1.count(i)


for i in new_dict:
    count.append(new_dict[i])


alldif = []

for key in new_dict:
    print(key, '->', new_dict[key])
    c = 0
    for i in list2:
        if i == key:
            c = c + 1
            if i != key+1 and c != new_dict[key]:
                alldif.append(key)

print(alldif, "printing alldif")



# c = 0
# newdict2 = {}
#
#
# for i in list2:
#     row = list2
#     if row[i] == i:
#         c = c + 1
#     if row[i+1] != i:
#         c = 0
#
#         alldif.append(list2)
#         print("found match")
#
#
# for i in list1:
#     for x in list2:
#         value1 = i
#         value2 = x
#         if value1 == value2:
#             c = c + 1
#             if value1 != x+1:
#                 c = 0
#
#
# print(alldif)
# print(list2)
# print(new_dict)
# print(count)
# print(c)


# def getdupcates(listOfElems):
#     ''' Get frequency count of duplicate elements in the given list '''
#     dictOfElems = dict()
#     # Iterate over each element in list
#     for elem in listOfElems:
#         # If element exists in dict then increment its value else add it in dict
#         if elem in dictOfElems:
#             dictOfElems[elem] += 1
#         else:
#             dictOfElems[elem] = 1
#
#             # Filter key-value pairs in dictionary. Keep pairs whose value is greater than 1 i.e. only duplicate elements from list.
#     dictOfElems = {key: value for key, value in dictOfElems.items() if value > 1}
#     # Returns a dict of duplicate elements and thier frequency count
#     return dictOfElems


