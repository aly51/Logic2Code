def modeAndFrequency(n: list[int]):
    dictionary={}

    for i in n:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i]=1

    mode=(0,0)

    for k,v in dictionary.items():
        if v > mode[1]:
            mode=(k,v)

    print(dictionary)

    for k,v in dictionary.items():
        if v == mode[1] and k != mode[0]:
            print("No mode in Array")
            return
    
    print(f"Mode: {mode[0]} Frequency of mode: {mode[1]}")

def main():
    n=int(input("Enter number of elements: "))
    arr=[]
    
    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    modeAndFrequency(arr)

if __name__ == "__main__":
    main()