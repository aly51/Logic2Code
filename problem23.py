import random

def LCS(l: list[int]):
    seen = set(l)
    sol = set()

    for i in seen:
        if i - 1 not in seen:
            temp = set()
            j = i

            while j in seen:
                temp.add(j)
                j += 1

            if len(temp) > len(sol):
                sol = temp

    return sol

def main():
    list1=[]
    for i in range(1000):
        list1.append(random.randint(-1000,1000))

    res=LCS(list1)
    print(sorted(res))

if __name__ == "__main__":
    main()