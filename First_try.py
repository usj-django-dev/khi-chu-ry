T = int(input("Write the test case number, T =  "))
if T <= 100:
    lst = []
    # n = int(input("Enter number of elements : "))
    for i in range(0, T):
        ele = str(input())
        lst.append(ele)
    print(lst)

else:
    print("The test case number will be less than 100")


