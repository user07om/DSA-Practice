

a = 4
b = 4
print(a == b) #False #equal to
print(a != b) #True #not equal to
print(a > b) #False #greater than
print(a < b) #True #less than
print(a >= b) #True #greater than equal to
print(a <= b) #True #less than equal to.



print("-----------------------")

grade = 10
# A >= 60 <= 80 if
# B >= 40 <= 60 elif
# C = else

if grade >= 60 <= 80:
    print('A')
elif grade >= 40:
    print('B')
elif grade == 10:
    print("well off")
else:
    print('Fail!')




print("WHile loop: ")
# 1.. 10 through while loop
"""
while cond:
    tasks
"""
i = 0
while i <= 5: #invalide this condition to stop.
    print("*"*i)
    i = i + 1


#flag = True
#while flag: #why is this executing: Flag? True.. so False exit!
#    print("Yo, i'm repeating myself!")
#    #voting system.
#    user_input = int(input("Enter 0 to exit! "))
#    if user_input == 0:
#        flag = False
        








    

#Output -> 0

"""
i = 0 -> print(0) -> 
i = 1 -> print(1)
i = 2 -> print(2)
i = 3 -> print(3)
i = 4 -> print(4)
i = 5 -> print(5)
i = 6 (condition 6 <= 5) False ->>>> exit
"""




# 1. person-name
names = ["omkar", "ayaan", "dnyanu", "harsh"]
cars = ["honda", "volvo", "maruti"]
#for loop only
#for name in names:
    #print(name)

# for loop for range(start, end, step)
#for i in range(len(names)):
    #print("Yoo Baby: ", names[i])
    #print(f"{i+1}: {names[i]}")


# for loop for enumerate()
#for i, name in enumerate(names):
    #print(i+1, name)

for var_name in zip(names, cars):
    print(var_name) #outut value is in tule format
    









#python -> compile -> .pyc -> PVM -> human readable.
