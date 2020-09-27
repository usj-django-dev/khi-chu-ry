T = input ('Write down the Test_Case number, T = ')

num = int(T)

if num <= 100:
    counter = 0
    while counter <= num:
        def reverseword(s):

            w = s.split(" ")
            nw = [i[::-1] for i in w]
            ns = " ".join(nw)
            return ns


        s = input("")
        if counter < num:
            print(reverseword(s))
        else:
            print("fuck you")
    count += 1


# else:
#         print("fucked")



    #
    # def reverseword(s):
    #     w = s.split(" ")
    #     nw = [i[::-1] for i in w]
    #     ns = " ".join(nw)
    #     return ns
    # s = input("")
    # print(reverseword(s))
    #
#     count = 0
#     while count < num:
#         if count == num:
#             print("You reached the limits")
#         else:
#             def reverseword(s):
#                 w = s.split(" ")
#                 nw = [i[::-1] for i in w]
#                 ns = " ".join(nw)
#                 return ns
#             s = input("")
#             # print(reverseword(s))
#     count += 1
else:
    print("The number of test case will be less than or equal 100 ")



# counter = 0
#
# while counter < 3:
#     print("Inside loop")
#     counter = counter + 1
# else:
#     print("Inside else")






# T = input ('rite down the Test_Case number, T =  ')
# num = int(T)
# if num <= 100:
#     print("we are now inside the if loops")
# else:
#     print("The number of test case will be less than or equal 100 ")

