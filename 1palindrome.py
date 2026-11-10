def is_palindrome(x):
    # type casting the number into str
    str_x = str(x)

    #comparing with the reverse of string
    if str_x == str_x[::-1]:
        return True
    else:
        return False

x = int(input("Enter a number: "))
print(is_palindrome(x))


def is_palindrome_math(x):
    real_no = x
    reverse_no = 0

    while x > 0:
        last_digit = x%10
        reverse_no = reverse_no * 10 + last_digit
        x = x//10
    return real_no == reverse_no

print(is_palindrome_math(x))