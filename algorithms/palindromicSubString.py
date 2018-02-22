

def longestPalindrome(s):
    list1 = []
    maxLength = 0
    list2 = []
    maxLength1 = 0
    for i in range(1, len(s)):
        a = palindromicSubString(i,s)

        if (a != []) and (len(a[0]) >= maxLength):
            if list1 == []:
                list1.append(a[0])
                maxLength = len(a[0])
            else:
                list1.pop()
                list1.append(a[0])
                maxLength = len(a[0])
    for i in range(1, len(s)):
        b = palindromicSubString1(i, s)
        if (b != []) and (len(b[0]) >= maxLength1):
            if list2 == []:
                list2.append(b[0])
                maxLength1 = len(b[0])
            else:
                list1.pop()
                list1.append(b[0])
                maxLength1 = len(b[0])


    msg = "0" if list1 == [] else list1[0]
    msg2 = "0" if list2 == [] else list2[0]

    return str(msg) if len(msg)>=len(msg2) else str(msg2)


def palindromicSubString(index,s):
    left = index-1
    right = index+1
    strng = []
    while (left >=0 and right<=len(s)-1):
        if s[left] == s[right]:
            if strng==[]:
                strng.append(s[left:right + 1])
            else:
                strng.pop()
                strng.append(s[left:right + 1])
            left -= 1
            right += 1
        else:
            break

    return strng

def palindromicSubString1(index,s):
    temp = s[index]
    increment = index
    strng = []
    while (increment<=(len(s)-2)):
        if temp==s[increment+1]:
            if strng==[]:
                strng.append(s[index:increment+2])
            else:
                strng.pop()
                strng.append(s[index:increment+2])
            increment += 1
        else:
            break
    return strng







print longestPalindrome("bb")

# print palindromicSubString1(2,"asbbbbbbyyy")

# print palindromicSubString(2,"babab")


def LCA(curr, A, B):
    if (curr==None):
        return curr
    if (curr==A or curr==B):
        return curr
    left = LCA(curr.left,A,B)
    right = LCA(curr.right,A,B)
    if (left!=None and right!=None):
        return curr
    if (left==None):
        return right
    else:
        return left



