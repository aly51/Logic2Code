import math
import random

class time:
    def __init__(self, hour, min, sec):
        self.hour=hour if hour >= 0 else print("not a valid hour")
        self.min=min if min < 60 and min >= 0 else print("not a valid minute")
        self.sec=sec if sec < 60 and sec >= 0 else print("not a valid second")

    def __str__(self):
        return f"{self.hour}:{self.min}:{self.sec}"

    def to_sec(self):
        return self.hour*3600 + self.min*60 + self.sec 

    def __ge__(self, other):
        return self.to_sec() >= other.to_sec()

    def __le__(self, other):
        return self.to_sec() <= other.to_sec()
    
    def __sub__(self, other):
        tim=(self.to_sec()) - (other.to_sec()) if self.to_sec() >= other.to_sec() else (other.to_sec()) - (other.to_sec())
        return time(math.floor(tim/3600), math.floor((tim%3600)/60), tim%60)

    def __truediv__(self, n:int):
        tim=self.to_sec()//n
        return time(math.floor(tim/3600), math.floor((tim%3600)/60), tim%60)
    
    def __add__(self, other):
        tim=(self.to_sec()) + (other.to_sec())
        return time(math.floor(tim/3600), math.floor((tim%3600)/60), tim%60)

def main():
    times=[]
    for i in range(100):
        h=random.randint(0,23)
        m=random.randint(0,59)
        s=random.randint(0,59)
        times.append(time(h,m,s))

    sum=time(0,0,0)
    for i in times:
        sum+=i
    average=sum/len(times)
    print(f"Average time: {average}")

    h1=int(input("Enter 1st time's Hour: "))
    m1=int(input("Enter 1st time's Minute: "))
    s1=int(input("Enter 1st time's Second: "))
    t1=time(h1,m1,s1)

    h2=int(input("Enter 2nd time's Hour: "))
    m2=int(input("Enter 2nd time's Minute: "))
    s2=int(input("Enter 2nd time's Second: "))
    t2=time(h2,m2,s2)

    count=0

    for i in times:
        if (i <= t1 and i >= t2) or (i >= t1 and i <= t2):
            count+=1

    print(f"{count} number of workwers worked in between the range")

if __name__=="__main__":
    main()