n1 = int(input("enter first number: "))
n2 = int(input("enter second number: "))
n3 = int(input("enter third number: "))

def formula():
    if n1 == n2 and n1 == n3 and n2 == n3:
        res5 = n1 * n2 * n3
        print(f"result is: {res5}")
    elif n1 == n2:
        res2 = (n1 * n2) + n3
        print(f"result is: {res2}")
    elif n1 == n3:
        res3 = (n1 * n3) + n2
        print(f"result is: {res3}")
    elif n2 == n3:
        res4 = (n2 * n3) + n1
        print(f"result is: {res4}")
    else:
        if n1 != n2:
            res1 = n1 + n2 + n3
            print(f"result is: {res1}")
        elif n1 != n3:
            res1 = n1 + n2 + n3
            print(f"result is: {res1}")
        elif n2 != n3:
            res1 = n1 + n2 + n3
            print(f"result is: {res1}")


    return

formula()
