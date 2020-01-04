# https://projecteuler.net/problem=35

import math

def IsPrime(num):
    sqrtNum = math.ceil(math.sqrt(num)) + 1
    for i in range(2, sqrtNum):
        if num % i == 0:
            return False
    if num == 2:
        return True
    if num == 1:
        return False
    return True

def Circles(num):
    numStr = str(num)
    numStrLen = len(numStr)
    circle = [1] * numStrLen
    for i in range(numStrLen):
        c = numStr[i:] + numStr[:i]
        circle[i] = int(c)
    return circle

def IsCircularPrime(num):
    circles = Circles(num)
    # print(circles)
    for circle in circles:
        if not IsPrime(circle):
            return False
    return True

circularPrimes = []
for i in range(1, 1000001):
    if IsCircularPrime(i):
        circularPrimes.append(i)


print(circularPrimes)
count = len(circularPrimes)
print(count)
