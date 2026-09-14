import math

def perfect_power(n: int):
    if n < 4:
        return

    for k in range(4, n+1):
        for i in range(2, int(math.sqrt(k))+1):
            j=2
            while pow(i, j) <= k:
                if pow(i,j) == k:
                    print(f"{k} = {i} ^ {j}")
                j += 1

def main():
    n=int(input("Enter a positive inreger: "))
    perfect_power(n)

if __name__=="__main__":
    main()