import math

def is_prime(n: int):
    if n < 2: 
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i==0:
            return False

    return True

def goldbach_conjecture(n: int):
    for i in range(4, n+1):
        if i%2 != 0:
            continue

        representations=0
        seenPrimes=set()
        print(i, end="  :  ")

        for j in range(2, n + 1):
            if is_prime(j) and j not in seenPrimes and is_prime(i - j):
                representations += 1
                print(f"{j} + {i - j}")
                seenPrimes.add(j)
                seenPrimes.add(i-j)

        print(f"Representations = {representations}")
            


def main():
    n=int(input("Enter a number : "))
    goldbach_conjecture(n)

if __name__=="__main__":
    main()