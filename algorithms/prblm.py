# def partition(arr, start, end):
#     index = start
#     pivot = arr[end]
#     for i in range(start, end):
#         if arr[i]<=pivot:
#             arr[i],arr[index] = arr[index],arr[i]
#             index+=1
#     arr[index],arr[end] = arr[end],arr[index]
#     return index
#
# def quicksort(arr,start,end):
#     if start < end:
#         p = partition(arr,start,end)
#         quicksort(arr,start,p-1)
#         quicksort(arr,p+1,end)
#
#     return arr
#
# list1 = [5,7,4,2,9,45,23,1,3,56,11,34]
#
# print quicksort(list1,0,11)

#
# def partition(arr, low, high):
#     i = (low - 1)  # index of smaller element
#     pivot = arr[high]  # pivot
#
#     for j in range(low, high):
#
#         # If current element is smaller than or
#         # equal to pivot
#         if arr[j] <= pivot:
#             # increment index of smaller element
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return (i + 1)
#
# def quickSort(arr, low, high):
#     if low < high:
#         # pi is partitioning index, arr[p] is now
#         # at right place
#         pi = partition(arr, low, high)
#
#         # Separately sort elements before
#         # partition and after partition
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)
#
#     return arr
#
# print quickSort([5,7,4,2,9,45,23,1,3,56,11,34,13],0,1

# nums = [5,7,4,2,9,45,23,1,3,56,11,34,13,4]
# d = {}
# for idx,num in enumerate(nums):
#     if num not in d:
#
#         d[num] = [idx]
#     else:
#         d[num].append(idx)
#
# print d
#
#
# def twoSum(nums):
#     num_dict = {}
#     for idx, num in enumerate(nums):
#         if num in num_dict:
#             num_dict[num].append(idx)
#         else:
#             num_dict[num] = [idx]
#     print(num_dict)
#
#
# twoSum(nums
# input1 = -120
#
# def f(input1):
#
#     x = ""
#     y = ""
#     for num in str(input1)[-1::-1]:
#         if num=="-":
#            x+=num
#         else:
#             y+=num
#     return int(x+y)
#
#
#
#
#
# d = {'x': 1, 'y': 2, 'z': 3}
# for key in d.values():
#     print key
#
# d = {'x': 1, 'y': 2, 'z': 3}
# for i, (key, value) in enumerate(d.items()):
#    print(i, key, value)

# list1 = []
# list2 = []


# def stringSlicing(start,strng,slicingIndex):
#     comp = strng[start]
#     for i in range(start+1,len(strng)):
#         if strng[i]==comp:
#             list1.append(strng[slicingIndex:i])
#             list2.append(strng[i:])
#             print strng
#             return strng
#     start = start+1
#     if len(strng)>start:
#         stringSlicing(start, strng, slicingIndex)
#
#
#
# print stringSlicing(0,"jkhcvroo",0)
#
#
# print list1
# print list2

