def self_descriptive(n: str):
    freq={}

    for i in range(len(n)):
        freq[i]=int(n[i])

    for i in range(len(n)):
        if freq[int(n[i])] > 0:
            freq[int(n[i])] = freq[int(n[i])] - 1
        else:
            return False

    return True        

def main():
    n=str(input("Enter a number: "))
    try:
        int(n)
    except:
        print("Enter a valid number")

    flag=self_descriptive(n) if int(n) > -1 else False
    print(f"{n} is self descriptive.") if flag else print(f"{n} is not self descriptive.")


if __name__=="__main__":
    main()