def reverse_num(num):
    revNum = 0
    while num>0:
        revNum = revNum*10 + num%10
        num = num//10

    return revNum


print reverse_num(1234)

print 451//10


def ReverseandAdd(num):
    rev_num = 0
    while (num <= 4294967295):
        # Reversing the digits of the number
        rev_num = reverse_num(num)

        # Adding the reversed number with the original
        num = num + rev_num

        # Checking whether the number is palindrome or not
        if reverse_num(num) == num :
            return num
        else:
            if (num > 4294967295):
                return "No palindrome exist"



print ReverseandAdd(143)