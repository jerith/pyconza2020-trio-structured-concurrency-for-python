n = int(input("HOW MANY PRIMES? "))
print(2)
primes = []
candidate = 3
while len(primes) < n-1:
    for p in primes:
        if candidate % p == 0:
            break
    else:  # Runs if the loop ends without breaking.
        primes.append(candidate)
        print(candidate)
    candidate += 2
