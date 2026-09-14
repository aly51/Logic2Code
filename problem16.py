def gcd(i: int, j: int):
    if j == 0:
        return i
    return gcd(j, i%j)

def totient(n: int):
    if n < 0:
        return
    
    print(f"Number coprime to {n}: ")
    coprimes=[]
    for i in range(1, n):
        if gcd(i,n) == 1:
            coprimes.append(i)
            print(i, end="  ")

    print()
    print(f"phi({n}) = {len(coprimes)}")

def main():
    n=int(input("Enter n: "))
    totient(n)

if __name__=="__main__":
    main()