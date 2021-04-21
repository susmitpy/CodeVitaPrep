"""
How to Execute : 
python3 app.py < input.txt 
python3 app.py < input1.txt 
"""

D, P = list(map(int, input().split(" ")))

def get_primes_till_n(n):
    primes = [2]

    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n+1)]
     
    p = 2
    while(p * p <= n):
          
        # If prime[p] is not changed, then it is
       # a prime
        if (prime[p] == True):
              
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    primes.extend([p for p in range(3,n,2) if prime[p]])
    return primes

duration_of_each_part = D // P
parts_starts = [i for i in range(1,D,duration_of_each_part)]
primes = get_primes_till_n(D)

c = 0
for d in range(duration_of_each_part):
    if all(list(map(lambda x: x+d in primes, parts_starts))):
        c+= 1

print(c)
