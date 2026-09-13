def look_and_say_generator(num: int):
    baseString="1"

    for i in range(num):
        print(f"{i+1}. {baseString}                (Length = {len(baseString)})")
        string=""
        j=0

        while j < len(baseString):
            count=1 
            while j+1 < len(baseString) and baseString[j]==baseString[j+1]:
                count += 1
                j += 1
            string+=str(count)+ baseString[j]
            j += 1

        baseString=string

def main():
    n=int(input("Enter number of terms: "))
    look_and_say_generator(n)

if __name__=="__main__":
    main()