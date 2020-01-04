from itertools import permutations 
from primes import primes

# perm = permutations([1, 2, 3]) 

def toInt(touple):
	ones = int(touple[3])
	tens = int(touple[2])
	hundreds = int(touple[1])
	thousands = int(touple[0])
	return thousands * 1000 + hundreds * 100 + tens * 10 + ones

def getTripletFromPerms(perms):
	perms_list = list(perms)
	int_perms_list = [] * len(perms_list)
	for perm in perms_list:
		if perm[0] != '0':
			int_perms_list.append(toInt(perm))

	# use int_perms_list from now on
	lent = len(int_perms_list) 
	for i in range(0, lent):
		for j in range(i + 1, lent):
			for k in range(j + 1, lent):
				if(abs(int_perms_list[i] - int_perms_list[j]) == 3330 and abs(int_perms_list[j] - int_perms_list[k]) == 3330 and int_perms_list[i] in primes and int_perms_list[j] in primes and int_perms_list[k] in primes):
					print(str(int_perms_list[i]) + " " + str(int_perms_list[j]) + " " + str(int_perms_list[k]))

def getTripletInRange(lo, hi):
	for num in range(lo, hi):
		num_as_list = list(str(num))
		perms = permutations(num_as_list)
		getTripletFromPerms(perms)
		# for perm in list(perms):
		# 	if perm[0] != '0':
				
		# 		# do stuff

		# 		print(toInt(perm))

triplet = getTripletInRange(1000, 9999)