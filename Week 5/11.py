import math

def calc_manhattan_dist(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

def ret_prime_factor(dist, ID):
    prime_factor_list = set()

    n = dist
    for i in range(2, int(math.sqrt(n))+1):
        while n % i == 0:
            prime_factor_list.add(i)
            n = n / i

    prime_factor_list = list(prime_factor_list)
    sorted(prime_factor_list)
    
    for i in prime_factor_list:
        if i > ID:
            return i
    
    return prime_factor_list[len(prime_factor_list)-1]


N = input()
M = input()
T = input() 

air_bases_list = []
target_list = []

for i in range(N):
    x = input
    y = input
    id = input
    air_bases_list.append(list(x, y, id))

for i in range(M):
    x = input
    y = input
    id = input
    target_list.append(list(x, y, id))

# This is incomplete!