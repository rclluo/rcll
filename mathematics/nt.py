calc_primes_upto=5000000
primes=[]

def prime_factorization(n: int) -> list[int]:
    global primes
    pf=[]
    if not len(primes):
        primes=find_primes(calc_primes_upto)
    for p in primes:
        if n%p==0:
            e=0
            while n%p==0:
                n//=p
                e+=1
            pf.append((p,e))
        if p*p>n: 
            break
    if n>1:
        pf.append((n,1))
    return pf

def find_primes(n: int) -> list[int]:
    if n<=2:
        return []
    sieve=list(range(3, n, 2))
    top=len(sieve)
    for si in sieve:
        if si:
            bottom=(si*si-3)//2
            if bottom>=top:
                break
            sieve[bottom::si]=[0]*-((bottom-top)//si)
    return [2]+[el for el in sieve if el]

def factor_count(n: int) -> int:
    pf=prime_factorization(n)
    num_factors=1
    for _, e in pf:
        num_factors*=(e+1)
    return num_factors

def euler_totient(n: int) -> int:
    pf=prime_factorization(n)
    ret=n
    for p, _ in pf:
        ret*=(p-1)
        ret//=p
    return ret
