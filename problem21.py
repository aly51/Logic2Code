import random

def pairSum(n: list[int], key: int):
    if not n:
        return
    set1=set()
    sol=set()
    for i in n:
        if key - i in set1:
            sol.add((i, key - i))

        set1.add(i)

    return sol

def main():
    list1=[]
    for i in range(100):
        list1.append(random.randint(-100,100))

    key=int(input("Enter key you want to search: "))
    res = pairSum(list1, key)
    print(res)

if __name__ == "__main__":
    main()