import math
def discoverShapes(n: int):
    l1 = set()

    for l in range(1, math.isqrt(n) + 1):
        if n % l != 0:
            continue

        remaining = n // l

        for w in range(l, math.isqrt(remaining) + 1):
            if remaining % w == 0:
                h = remaining // w
                l1.add((l, w, h))

    print(f"Total number of cuboids: {len(l1)}")

    min_surface = math.inf
    max_surface = 0

    for l, w, h in l1:
        surface = 2 * (l * w + l * h + w * h)

        print(f"Surface area of cuboid {l} {w} {h}: {surface}")

        if l==w and w==h:
            print(f"{n} can create a cube")

        if surface < min_surface:
            min_surface = surface

        if surface > max_surface:
            max_surface = surface

    print(f"Minimum surface area: {min_surface}")
    print(f"Maximum surface area: {max_surface}")

def main():
    n=int(input("Enter a positive integer: "))
    if n <= 0:
        print("Enter valid number")
        return

    discoverShapes(n)

if __name__ == "__main__":
    main()