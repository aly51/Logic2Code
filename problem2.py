def digital_root(n: int):
    if n < 1:
        return 
    
    while n > 9:
        num=0
        while n > 0:
            num += n%10
            n = n//10

        n=num

    return n

def digital_root_frequency(n: int):
    frequency={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

    for i in range(1, n+1):
        root=digital_root(i)
        frequency[root] += 1
    
    print(frequency)
    
def main():
    num=int(input("Enter a positive integer: "))
    digital_root_frequency(num)

if __name__ == "__main__":
    main()