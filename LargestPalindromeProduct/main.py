# https://projecteuler.net/problem=4
# Find the largest palindrome made from the product of two 3-digit numbers.

def IsPalindrome(num):
    numStrList = list(str(num))
    revNumStrList = numStrList.copy()
    numStrList.reverse()
    if numStrList == revNumStrList:
        return True
    return False



# for num1 in range(99, 9, -1):
#     for num2 in range(99, 9, -1):
#         prod = num1 * num2
#         if IsPalindrome(prod):
#             print(prod)


palindromes = []

for num1 in range(999, 99, -1):
    for num2 in range(999, 99, -1):
        prod = num1 * num2
        if IsPalindrome(prod):
            palindromes.append(prod)
            print(prod, num1, num2)

res = max(palindromes)
print(res)