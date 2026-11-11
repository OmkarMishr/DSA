def SPSD(n):
    sum = 0
    prod = 1
    while n != 0:
        last_digit = n%10
        n = n//10
        sum = sum + last_digit
        prod =  prod * last_digit
    return prod - sum


n = int(input("Enter a number: "))
print(SPSD(n))