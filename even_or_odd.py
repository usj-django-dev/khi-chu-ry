T = int(input("Write the test case number, T =  "))
if 1 <= T <= 100:

    for i in range(0, T):
        mod = i % 2
        if mod > 0:
            print("This is an odd number.")
        else:
            print("This is an even number.")


else:
    print("The test case number will be less than 100")


#
# while number < 5 :
#     print("Thank you")
#     # Increment the value of the variable "number by 1"
#     number = number+1





#
# counter = 0
#
# while counter < T:
#     print("Inside loop")
#     counter = counter + 1
# else:
#     print("Inside else")








# first success:
# T = int(input("Write the test case number, T =  "))
# if T <= 100:
#     lst = []
#     # n = int(input("Enter number of elements : "))
#     for i in range(0, T):
#         ele = str(input())
#         lst.append(ele)
#     print(lst)
#
# else:
#     print("The test case number will be less than 100")
