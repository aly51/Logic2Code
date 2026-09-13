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

def main():    
    n=int(input("Enter a positive number: "))
    for i in range(1, n+1):
        print_collatz(i)
        print()

if __name__ == "__main__":
    main()