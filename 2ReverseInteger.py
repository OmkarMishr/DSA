def Reverse(x):
    if x > 0 :
        sign = 1
    else:
        sign = -1
    x = abs(x)
    reverse = 0
    while x != 0:
        last_digit = x%10
        reverse = reverse*10+last_digit
        x = x//10
    result = sign * reverse
    if result < -2147483648 or result > 2147483647:
        return 0
    return result

a = int(input("Enter a number:"))
print(Reverse(a))