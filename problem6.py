import random
def recurring_decimal_cycle(neumrator: int, denominator: int):
    remainders=[]
    remainder=neumrator%denominator
    count=0
    while  remainder!= 0:
        if remainder in remainders:
            return count - remainders.index(remainder)
        
        remainders.append(remainder)
        remainder=(remainder*10)%denominator
        count += 1
        
    return 0




def main():
    n=int(input("Enter number of fractions: "))
    maxLen=(0,0,0)
    
    for i in range(n):
        neumrator=random.randint(-1000,1000)
        denominator=random.randint(1,1000)
        print(f"{neumrator}/{denominator}", end="  ")
        len=recurring_decimal_cycle(neumrator, denominator)
        maxLen=(len,neumrator,denominator) if len > maxLen[0] else maxLen
        print(f"length of cycle is {len}")

    print(f"{maxLen[1]}/{maxLen[2]} has longest cycle with length {maxLen[0]}")

if __name__ == "__main__":
    main()