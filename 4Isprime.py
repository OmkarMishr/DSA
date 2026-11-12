#Brute Force Approch 

# def Isprime(n):
#     for i in range(2,int((n**0.5)+1)):
#         if n%i == 0:
#             return False
#     return True


# n = int(input("Enter a number: "))
# print(Isprime(n))

# def count_primes(n):
#     count_prime = 0
#     for i in range(2,n):
#         if Isprime(i):
#             count_prime = count_prime + 1
#     return count_prime

# print(count_primes(n))


# Optimized Approach

def Isprime(n):
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
  

    for i in range(2,int((n**0.5)+1)):
        if is_prime[i] == True:
            for j in range(i*i,n,i):
                is_prime[j] = False
    count_prime = 0
    for val in is_prime:
      if val == True:
        count_prime = count_prime + 1
    return count_prime


n = int(input("Enter a number: "))
print(Isprime(n))