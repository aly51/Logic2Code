import random

def gcd(i: int, j: int):
    if j == 0:
        return i
    return gcd(j, i%j)

def taskSync(N:int, h:int, m:int):
    arr=[]
    for i in range(N):
        arr.append(random.randint(5,60))

    results=[]
    for i in range(N - 1):
        if i == 0:
            lcm=(arr[i] * arr[i+1])//gcd(arr[i], arr[i+1])
            results.append(lcm)
        else: 
            lcm=(results[i-1] * arr[i+1])//gcd(results[i-1], arr[i+1])
            results.append(lcm)

    nm = (m + lcm) % 60
    hc = (m+lcm) // 60
    nh = (h + hc) % 24
    dc = (h + hc) // 24

    for i in range(N):
        print(f"Task {i + 1} : {arr[i]}")
    print(f"Sync Interval: {lcm}")
    print(f"Day {dc}")
    print("at")
    print(f"{nh}:{nm}")
    


def main():
    N=int(input("Enter number of tasks: "))
    h=int(input("Enter startig hour: "))%24
    m=int(input("Enter starting minutes: "))%60
    taskSync(N,h,m)

if __name__=="__main__":
    main()