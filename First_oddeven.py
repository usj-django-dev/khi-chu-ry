
T = int(input("Write the test case number, T =  "))
if T <= 100:
    for i in range(0, T):
        n = int(input())
        if 0 <= n <= 2147483647:
            q = n % 2
            if q > 0:
                print("odd")
            else:
                print("even")
        else:
            print("The will be 0<=n<=2147483647")
else:
    print("The test case number will be 1<=T<=100")

