# based largely on the prime number generator here: 
#  https://www.geeksforgeeks.org/how-to-generate-large-prime-numbers-for-rsa-algorithm/

import random
import timeit
import cryptomath

def first_primes_list():
    """return list the first 90 or so prime numbers"""
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
            31, 37, 41, 43, 47, 53, 59, 61, 67, 
            71, 73, 79, 83, 89, 97, 101, 103, 
            107, 109, 113, 127, 131, 137, 139, 
            149, 151, 157, 163, 167, 173, 179, 
            181, 191, 193, 197, 199, 211, 223,
            227, 229, 233, 239, 241, 251, 257,
            263, 269, 271, 277, 281, 283, 293,
            307, 311, 313, 317, 331, 337, 347, 349]

def nBitRandom(n):
    return random.randrange(2**(n-1)+1, 2**n - 1)

def getLowLevelPrime(n):
    '''Generate a prime candidate divisible by first primes'''
    while True:
        # Obtain a random number
        pc = nBitRandom(n) 
  
         # Test divisibility by pre-generated 
         # primes
        for divisor in first_primes_list():
            if pc % divisor == 0 and divisor**2 <= pc:
                break
        else: return pc

def isMillerRabinPassed(mrc):
    '''Run 20 iterations of Rabin Miller Primality test'''
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == mrc-1)
  
    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                return False
        return True
  
    # Set number of trials here
    numberOfRabinTrials = 20 
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True

def Private_d(e, p, q):
    return cryptomath.findModInverse(e, (p -1) * (q -1))
    

def RandomRSAPrimeNumber(DesiredBits=1024):
    num_candidates = 0
    start_time= timeit.default_timer()
    n = DesiredBits
    candidate = 0

    while True:
        prime_candidate = getLowLevelPrime(n)
        num_candidates += 1
        if not isMillerRabinPassed(prime_candidate):
            continue
        else:
            candidate = prime_candidate
            break
    end_time = timeit.default_timer()

    return dict(prime_number=candidate, elapsed_seconds=(end_time-start_time), number_candidates=num_candidates)

def SequentialRSAPrimeNumbers(DesiredBits=1024, NumberOfPrimes=10):
    found_primes = []
    first_prime = RandomRSAPrimeNumber(DesiredBits)
    found_primes.append(first_prime)
    
    while len(found_primes) < NumberOfPrimes:
        prime_candidate = found_primes[-1]["prime_number"]
        pc_start = timeit.default_timer()
        pc_candidatecount = 0
        while True:
            prime_candidate += 2
            pc_candidatecount += 1
            if not isMillerRabinPassed(prime_candidate):
                continue
            else:
                pc_end = timeit.default_timer()
                p = dict(prime_number=prime_candidate, elapsed_seconds=(pc_end-pc_start), number_candidates=pc_candidatecount)
                found_primes.append(p)
                break
    
    return found_primes