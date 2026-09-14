import math

def is_prime(n: int):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i==0:
            return False

    return True


def prime_gap(n: int):
    if n < 2:
        print("No prime Numbers")
    
    lastPrime=2
    for i in range(3, n+1):
        if is_prime(i):
            print(i - lastPrime, end=",")
            lastPrime=i

def main():
    n=int(input("Enter a number : "))
    prime_gap(n)

if __name__=="__main__":
    main()