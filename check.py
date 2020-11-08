# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")
#
#
#

T = int(input("Write the test case number, T =  "))
if T <= 100:
    # lst = []
    # n = int(input("Enter number of elements : "))
    for i in range(0, T):
        ele = int(input())
        q = ele % 2

        # lst.append(q)
    # for i in range(0, T):
        if q > 0:
            print("odd")
        else:
            print("even")

    # print(lst)


else:
    print("The test case number will be less than 100")

