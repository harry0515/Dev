#
#
# list = [5,7,4,2,9,45,23,1,3,56,11,34,13]
#
# def selectsorting(list):
#     for i in range(len(list)-1):
#         for j in range(i+1, len(list)):
#             if list[j] < list[i]:
#                 temp = list[j]
#                 list[j] = list[i]
#                 list[i] = temp
#     return list
#
# print selectsorting(list)
#
#
#
#
# list1 = [5,7,4,2,9,45,23,1,3,56,11,34,13]
#
# def bubblesorting(list):
#     for j in range(len(list)):
#         for i in range(len(list)-(1+j)):
#             if list[i] > list[i+1]:
#                 temp = list[i+1]
#                 list[i+1] = list[i]
#                 list[i] = temp
#     return list
#
# print bubblesorting(list1)
#
#
#
# list2 = [5,7,4,2,9,45,23,1,3,56,11,34,13]
#
#
# def insertionSorting(list):
#     for hole in range(1,len(list)-1):
#         value = list[hole]
#         while (hole>0 and (list[hole-1]>value)):
#             list[hole] = list[hole-1]
#             hole = hole-1
#         list[hole] = value
#
#     return list
#
# print insertionSorting(list2)
#
#


list1 = []
list2 = []


def stringSlicing(start,strng,slicingIndex):
    comp = strng[start]
    for i in range(start+1,len(strng)):
        if strng[i]==comp:
            list1.append(strng[slicingIndex:i])
            list2.append(strng[i:])
            print strng
            return strng
    start = start+1
    if len(strng)>start:
        stringSlicing(start, strng, slicingIndex)



print stringSlicing(0,"jkhcvroo",0)


print list1
print list2
print ord('t')