def descending(num: int):
    digits=str(num)
    number=0
    while len(digits) < 4:
        digits+='0'

    for i in range(4):
        maximum=max(digits)
        number += int(maximum)
        number *= 10
        digits=digits.replace(maximum,"",1)
    
    return number//10

def ascending(num: int):
    digits=str(num)
    number=0
    while len(digits) < 4:
        digits+='0'
        
    for i in range(4):
        minimum=min(digits)
        number += int(minimum)
        number *= 10
        digits=digits.replace(minimum,"",1)
    
    return number//10

def kaprekar_constant(num: str):
    if (num[0] == num[1] == num[2] == num[3]) or len(num) > 4:
        print("Enter non recurring 4 digits") 
        return
    
    try:
        num=int(num)
    except:
        print("Enter a number")
    
    while num != 6174:
        asc=ascending(num)
        desc=descending(num)
        num=desc-asc
        print(f"{desc} - {asc} = {num}") 

def main():
    num=str(input("Enter a four digit non repeating number: "))
    kaprekar_constant(num)

if __name__ == "__main__":
    main()