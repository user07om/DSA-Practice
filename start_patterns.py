# n = 5

# print("Pattern 1: Increasing numbers")
# for row in range(n):   #---- nth outer loop run krnar
#     for col in range(row): #---inner loop - row+1, 
#         print("**", end=" ")  #---add start and end 
#     print()

# # print()

# # for row in range(n):
# #     print("* "*row)

# for i in range(10, 0, -2):
#     print(i)

# for row in range(n):
#     for col in range(row):
#         print("*", end=" ")
#     print()



# # for i in range(1, n)
# # """
# # * * *
# # * *
# # * 
# # """
 

n = 6
for row in range(1, n+1):
    for col in range(n):
        if col < n-row:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()