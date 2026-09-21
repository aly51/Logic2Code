import numpy as np
def diagonalDifference(matrix: list[list[int]]):
    pd, sd = 0,0
    for i in range(len(matrix)):
        pd += matrix[i][i]
        sd += matrix[i][len(matrix)-i-1]

    return pd, sd, abs(pd - sd)

def main():
    n=int(input("Enter order of square matrix: "))
    if n < 0:
        print("Enter valid number")
        return
    
    matrix=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            element = int(input(f"Enter {i+1}, {j+1} element: "))
            matrix[i][j] = element

    pd,sd,dd=diagonalDifference(matrix)
    print(f'''Primary diagonal = {pd}
    Secondary diagonal = {sd}
    Diagonal difference = {dd}''')

if __name__ == "__main__":
    main()