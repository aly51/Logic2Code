def print_collatz(n: int):
    if n<1: 
        return
    
    while n != 1:
        if n%2 == 0:
            print(n, end=" -> ")
            n=n//2
        else:
            print(n, end=" -> ")
            n=3*n+1 
    print(1)

def collatz_length(n: int):
    if n<1: 
        return
    
    length=1
    while n != 1:
        if n%2 == 0:
            length += 1
            n=n//2
        else:
            length += 1
            n=3*n+1 
    return length

def main():
    length=(0,0)
    n=int(input("Enter a positive integer: "))
    for i in range(1, n+1):
        len=collatz_length(i)
        length=length if length[1]>len else (i,len)
    print(f"The longest collatz length in first {n} numbers belongs to {length[0]} with length {length[1]} the sequence being: ")
    print_collatz(length[0])

if __name__ == "__main__":
    main()