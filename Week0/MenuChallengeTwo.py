def print_matr():
    matr = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"] ]
    for x in matr:
        print(*x)

def swap():
    a = int(input("Enter a number "))
    b = int(input("Enter a number "))
    if a > b:
        print(b,a)
    else:
        print(a,b)