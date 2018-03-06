import math

def min_coin(total):
    noOf5coins = total//5
    noOf3coins = (total -(noOf5coins*5))//3
    noOf1coins = (total-(noOf5coins*5) - (noOf3coins*3))
    return (noOf5coins+noOf3coins+noOf1coins)


print min_coin(48)


def give_last_word(string1):
    list = string1.split(" ")
    return list[-2]


print give_last_word("git init // to create a repository in project file.")


# print int("1111", 10)
#  converting binary to decimal

def binary_decimal(string1):
    i = 0
    sum =0
    for num in string1[-1::-1]:
        sum = sum + int(num)*(2**i)
        i += 1

    return sum


print binary_decimal("111")


def hexadecimal(string1):
    i = 0
    sum =0
    for num in string1[-1::-1]:
        if int(num):
            num = sum + int(num, 16)*(16**i)
            i +=1
        else:
            pass

    return sum

def repeated(string1):
    list1 = []
    for i in range(len(string1)):
        if string1[i] not in list1:
            list1.append(string1[i])

    return "".join(list1)


print repeated("abcabcabcabcabcabc")

def prime(num):
    if num > 1:
        if num ==2:
            return " %d is a prime number" % (num)
        for i in range(2, num):
            if (num % i) == 0:
                return " %d is not a prime number" % (num)

    return " %d is a prime number" % (num)


print prime(675)

def amstrong(num):
    temp = num
    l = len(str(num))
    sum = 0
    while num > 0:
        number = num%10
        num = num//10
        sum = sum + (number**l)

    print sum
    if sum == temp:
        return True
    else:
        return False


print amstrong(153)



def last_int(list1,list2):


    l = min(len(list1),len(list2))

    for i in range(l):
        if list1[len(list1)-i-1]==list2[i]:
            print list2[i]

        if list1[len(list1)-i-1]>list2[i]:
            print list1[len(list1)-i-1]
            print list2[i]

        if list1[len(list1)-i-1]<list2[i]:
            print list2[i]
            print list1[len(list1)-i-1]

    if len(list1)<=l and len(list2)>l:
        for i in list2[l:]:
            print i

    elif len(list2)<=l and len(list1)>l:
        for i in list1[:len(list1)-len(list2)]:
            print i

def make_dict():
    d = {}
    strng = "abcdefghkijklmnopqrstuvwxyz"
    for i, num in enumerate(strng):
        d[num]=i
    return d


def small_letter(string1):
    d = make_dict()
    list1 = list(string1)
    print list1
    for num in list1:
        if num in d.keys():
            print d[num]
        else:
            print "None"




list1=[1,2,3,4]
list2 =[3,5,6,7]

last_int(list1,list2)

small_letter("bhhbhbhgQPPPP")

