class Utilities:

    def findDuplicatesofTser (list1, list2):

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


        extraones = []
        alldif2 = {}

        for key in dict1:
            c = 0
            for i in list2:
                if i == key:
                    c = c + 1
                    if i == key and c != dict1[key]:
                        alldif2 = + key, c - dict1[key]
                        for k in dict1.keys():
                            if i != k:
                                extraones.append(k)


        return  alldif2