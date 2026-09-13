def digital_root(n: int):
    if n < 1:
        return 
    presistence=0
    while n > 9:
        num=0
        while n > 0:
            num += n%10
            n = n//10
        n=num
        presistence += 1
    return n,presistence

def main():
    number=int(input("Enter a positive integer: "))
    root, presistence=digital_root(number)
    print(f"Root: {root}, Presistence: {presistence}")

if __name__ == "__main__":
    main()