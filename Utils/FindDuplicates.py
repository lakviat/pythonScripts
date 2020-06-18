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
##converting dictionary into map just in case
#newmap = dict(zip(dict1, map(int, dict1.values())))
#print(newmap , 'this is new map')
# if list1 has number 1's two times, then take only two times number 1's from list2
#i do have count now, i need to match count with list2, to do that i need to find coun of each element in the loop

list2 = [11, 11, 22, 22, 33, 33, 44, 44, 44, 44, 44, 55, 55, 55]
list1 = [11, 11, 22, 22, 33, 33, 44, 44, 55]
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

for i in dict1:
    print(i, 'list1 count -> ', dict1[i])

print()
for i in dict2:
    print(i, 'list2 count -> ', dict2[i])



alldif2 = {}
alldif3 = {}
extraones = []

for key in dict1:
    c = 0
    for i in list2:
        if i == key:
            c = c + 1
            if i == key and c != dict1[key]:
                alldif2 =+ key, c - dict1[key]
                for k in dict1.keys():
                    if i != k:
                        extraones.append(k)

list = alldif2
print(alldif2)
print(alldif3)

