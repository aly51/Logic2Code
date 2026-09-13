def check_happy_number(n: int):
    if n<1:
        return
    
    num=n
    seen=set()
    while num!=1 and num not in seen:
        number=0
        seen.add(num)
        while num > 0:
            number += (num%10)**2
            num=num//10
            
        num=number

    if num == 1:
        return True
    else: 
        return False

def main():   
    num=int(input("Enter a positive integer: "))
    print(f"{num} is a happy number.") if check_happy_number(num) else print(f"{num} is not a happy number.") 

if __name__ == "__main__":
    main()