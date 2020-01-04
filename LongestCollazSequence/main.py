# https://projecteuler.net/problem=14

import time

# using pure Iter
def collazIter(num):
    if num == 1:
        return 1
    if num & 1 == 0:
        num = num >> 1
    else:
        num = 3 * num + 1
    return num

def longestCollatzUnderIter(num):
    maxIndex = 1
    for i in range(1, num + 1):
            solution[i] = collazLenIter(i)
            if solution[i] > solution[maxIndex]:
                maxIndex = i
    return maxIndex
    
def collazLenIter(num):
    count = 0
    while num != 1:
        num = collazIter(num)
        count += 1
    return count

# using DP
solution = [0, 1] + [-1] * 1000000
def collazDP(num):
    if num == 1:
        return 1
    if num & 1 == 0:
        num = num >> 1
    else:
        num = 3 * num + 1
    return num

def longestCollatzUnderDP(num):
    maxIndex = 1
    for i in range(1, num + 1):
            solution[i] = collazLenDP(i)
            if solution[i] > solution[maxIndex]:
                maxIndex = i
    return maxIndex
    
def collazLenDP(num):
    count = 0
    while num != 1:
        num = collazDP(num)
        count += 1
    return count


limit = 500000
t1 = time.time()
sol = longestCollatzUnderIter(limit)
t2 = time.time()
print("pure iterative: " + str(sol) + " " + str(t2 - t1) + "s")

t1 = time.time()
sol = longestCollatzUnderDP(limit)
t2 = time.time()
print("DP + iterative: " + str(sol) + " " + str(t2 - t1) + "s")
