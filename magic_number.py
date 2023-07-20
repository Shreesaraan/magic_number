def magic_number(number):
    array=list(str(number))
    sum=0
    while number>0:
        sum+=number%10
        number//=10
    # for i in range(len(array)):
    #     sum+=int(array[i])
    if sum>9:
        return magic_number(sum)
    else:
        if sum==1:
            return 1
        else:
            return 0

number=int(input("Enter the Number : "))
print(magic_number(number))