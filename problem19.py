import math

class time:
    def __init__(self, hour, min, sec):
        self.hour=hour if hour < 24 and hour >= 0 else print("not a valid hour")
        self.min=min if min < 60 and min >= 0 else print("not a valid minute")
        self.sec=sec if sec < 60 and sec >= 0 else print("not a valid second")

    def __str__(self):
        return f"{self.hour}:{self.min}:{self.sec}"

    def __gt__(self, other):
        if self.hour > other.hour:
            return self
        elif self.hour==other.hour:
            if self.min > other.min:
                return self
            elif self.min==other.min:
                if self.sec>=other.sec:
                    return self
                else:
                    return other
            else:
                return other
        else:
            return other

    def __sub__(self, other):
        if self >= other:
            if self.sec >= other.sec:
                newSec=self.sec-other.sec
            else:
                newSec=(self.sec+60)-other.sec
                self.min -= 1

            if self.min >= other.min:
                newMin=self.min-other.min
            else:
                newMin=(self.min+60)-other.min
                self.hour -= 1

            newHour=self.hour-other.hour

        else:
            if other.sec >= self.sec:
                newSec=other.sec-self.sec
            else:
                newSec=(other.sec+60)-self.sec
                other.min -= 1

            if other.min >= self.min:
                newMin=other.min-self.min
            else:
                newMin=(other.min+60)-self.min
                other.hour -= 1

            newHour=other.hour-self.hour

        return time(newHour, newMin, newSec)

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
