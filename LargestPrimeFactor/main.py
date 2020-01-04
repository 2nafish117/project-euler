import math

def IsPrime(num):
    sqrtNum = math.ceil(math.sqrt(num))
    for i in range(2, sqrtNum):
        if num % i == 0:
            return False
    return True

def LargestPrimeFactor(num):
    sqrtNum = math.ceil(math.sqrt(num))
    for i in range(sqrtNum, 1, -1):
        if IsPrime(i):
            if num % i == 0:
                return i
            
lpf = LargestPrimeFactor(600851475143)
print(lpf)