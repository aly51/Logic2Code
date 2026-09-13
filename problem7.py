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
    maxLen=(0,0)
    for i in range(2, n+1):
        print(f"1/{i}", end="  ")
        len=recurring_decimal_cycle(1, i)
        maxLen=(len,i) if len > maxLen[0] else maxLen
        print(f"length of cycle is {len}")
    print(f"1/{maxLen[1]} has longest cycle with length {maxLen[0]}")

if __name__ == "__main__":
    main()