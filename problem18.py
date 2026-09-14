import math

class time:
    def __init__(self, hour, min, sec):
        self.hour=hour if hour < 24 and hour >= 0 else print("not a valid hour")
        self.min=min if min < 60 and min >= 0 else print("not a valid minute")
        self.sec=sec if sec < 60 and sec >= 0 else print("not a valid second")

    def __str__(self):
        return f"{self.hour}:{self.min}:{self.sec}"

    def __sub__(self, other):
        h1=self.hour*3600
        m1=self.min*60
        h2=other.hour*3600
        m2=other.min*60
        tim=(h1+m1+self.sec) - (h2+m2+other.sec)
        return time(math.floor(tim/3600), math.floor((tim%3600)/60), tim%60)

def main():
    h1=int(input("Enter 1st time's Hour: "))
    m1=int(input("Enter 1st time's Minute: "))
    s1=int(input("Enter 1st time's Second: "))
    t1=time(h1,m1,s1)

    h2=int(input("Enter 2nd time's Hour: "))
    m2=int(input("Enter 2nd time's Minute: "))
    s2=int(input("Enter 2nd time's Second: "))
    t2=time(h2,m2,s2)

    t3 = t1 - t2

    print(t3)


if __name__=="__main__":
    main()
