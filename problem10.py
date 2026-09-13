import math
def is_perfect_number(num: int):
    if num < 2:
        return False
    roots=[1]
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            roots.append(i)
            if i != num//i:
                roots.append(num//i)

    if sum(roots)==num:
        return True
    else:
        return False

def main():
    n=int(input("Enter nmber to verify: "))
    print(f"{n} is a perfect number")if is_perfect_number(n) else print(f"{n} is not a perfect number")

if __name__ =="__main__":
    main()