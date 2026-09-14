def num_of_divisors(n: int):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count += 1
    return count

def highly_composite(n: int):
    if n < 1:
        return

    highlyComposite={1:1}
    lastComposite=1
    for i in range(2, n + 1):
        divisors=num_of_divisors(i)
        if divisors > highlyComposite[lastComposite]:
            highlyComposite[i]=divisors
            lastComposite=i

    print(highlyComposite)
        

def main():
    n=int(input("Enter a positive integer: "))
    highly_composite(n)

if __name__=="__main__":
    main()