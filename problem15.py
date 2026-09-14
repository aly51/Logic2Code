import math

def sum_of_divisors(num: int):
    if num < 2:
        return 0
    roots=[1]
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            roots.append(i)
            if i != num//i:
                roots.append(num//i)

    return sum(roots)

def amicable_pairs(n: int):
    amicablePairs=set()

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if sum_of_divisors(i) == j and sum_of_divisors(j) == i:
                amicablePairs.add((i,j))

    return amicablePairs


def main():
    n=int(input("Enter upper limit: "))
    res=amicable_pairs(n)
    for i in res:
        print(f"{i[0]} <-> {i[1]}")

if __name__=="__main__":
    main()