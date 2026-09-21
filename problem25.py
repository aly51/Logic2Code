import math
def discoverShapes(n: int):
    l = set()

    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            l.add((i, n // i))

    print(f"Total number of rectangles: {len(l)}")
    
    min_perimeter = math.inf
    max_perimeter = 0

    for i in l:
        perimeter = 2 * (i[0] + i[1])
        print(f"Perimeter of rectangle {i[0]} {i[1]}: {perimeter}")

        if i[0] == i[1]:
            print(f"{n} can create a square")

        if perimeter < min_perimeter:
            min_perimeter = perimeter

        if perimeter > max_perimeter:
            max_perimeter = perimeter

    print(f"Minimum perimeter is: {min_perimeter}")
    print(f"Maximum perimeter is: {max_perimeter}")

     
def main():
    n=int(input("Enter a positive integer: "))
    if n <= 0:
        print("Enter valid number")
        return

    discoverShapes(n)

if __name__ == "__main__":
    main()