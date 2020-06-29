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
# converting dictionary into map just in case
# newmap = dict(zip(dict1, map(int, dict1.values())))
# print(newmap , 'this is new map')
# if list1 has number 1's two times, then take only two times number 1's from list2
# i do have count now, i need to match count with list2, to do that i need to find coun of each element in the loop

list2 = [11, 11, 22, 22, 33, 33, 44, 44, 44, 44, 44, 55, 55, 55]
list1 = [11, 11, 22, 22, 33, 33, 44, 44, 55]

if len(list2) > len(list1):
    print("list2 is bigger")
else:
    print("list1 is bigger")

dict1 = {}
dict2 = {}
count1 = []
count2 = []

for i in list1:
    dict1[i] = list1.count(i)
    count1.append(dict1[i])

for i in list2:
    dict2[i] = list2.count(i)
    count2.append(dict2[i])

print(dict1, count1)
print(dict2, count2)


alldif2 = {}
extraones = []

for key in dict1:
    c = 0
    for i in list2:
        if i == key:
            c = c + 1
            if i == key and c != dict1[key]:
                alldif2[i] = c - dict1[key]
                for k in dict1.keys():
                    if i != k:
                        extraones.append(k)


numberoftimestoremove = []
counts = []
cs = 0
for k in alldif2.values():
    cs = cs + 1
    if k > 0:
        numberoftimestoremove.append(k)
        counts.append(cs)


# This Function will catch TSER_ITEM_IDS in case its not present in diff env
findtseritemidsthatarenotpresent = []
for item in dict1.keys():
    if item not in dict2.keys():
        findtseritemidsthatarenotpresent.append(item)

if len(findtseritemidsthatarenotpresent) == 0:
    print("ALL TSER ITEM IDS MATCHING")
else:
    print("THESE TSER ITEMS ARE NOT PRESENT:", findtseritemidsthatarenotpresent)

print(numberoftimestoremove, 'NUMBER OF TIMES NEEDS TO BE REMOVED FROM LONGEST LIST')


#THIS FUNCTION FINDS THE DIFFERENCES ACCORDING TO COUNT IN BETWEEN TWO DICT
tseritemdifferences = []
for key in set(dict1) & set(dict2):
    if dict1[key] != dict2[key]:
        tseritemdifferences.append(key)


print(tseritemdifferences, 'THESE ARE TSER ITEMS HAVE DIFFERENCES', "TIMES")
print(numberoftimestoremove)

print(numberoftimestoremove, 'NUMBER OF TIMES NEEDS TO BE REMOVED FROM LONGEST LIST')

cyt = 0
# 44 i need to remove 3 times and 55 i need to remove 2 times
# 44
kotok = 0
for i in tseritemdifferences:
    if i in list2:
        cyt = cyt + 1
        cit = numberoftimestoremove[kotok]
        kotok = kotok + 1
        indexes = 0
        while indexes != cit:
            list2.remove(i)
            indexes = indexes + 1
            continue
        else:
            continue


print(tseritemdifferences, 'this is tseritem differences')
print("result should be 44 : 2 55 : 1")
print('this is a new list2\n')
print(list2)



