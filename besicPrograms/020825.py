
#REVERSE A STRING...

input_str = "omkar"
print(input_str[::-1])


# another approach
rev_str = ""
for i in range(len(input_str), 0, -1):
  rev_str += input_str[i-1]
  if len(rev_str) == len(input_str):
    print(rev_str)



#FIND THE MAX VALUE IN A LIST.
ele = [8, 2, 4, 1, 5]
max_v = 0
for i in range(len(ele)):
  if ele[i] >= max_v:
    max_v = ele[i]

print("max value is: ", max_v)


#SUM OF THE FIRST 10 NUMBERS IN 1-ANY.

input_number = 23
stop_sum_range = 10
sum_is = 0
for i in range(1, input_number+1):
  sum_is += i
  if stop_sum_range == i:
    break;

print(sum_is)


#CHECK IF NUMBER IS EVEN OR ODD...
input_num = 9
print("even") if input_num%2==0 else print("odd")


#get the cound of vovels in word/sentence.
count = 0
for i in range(len(input_str)):
  if input_str[i] in "aeiou":
    count+=i

print(f"the count of vovels in the input str: ", count)



#check pali string:
inpStr = "racecar"
print("palindrom") if inpStr[::-1] == inpStr else print("not palindrom")



#get the factorial
fact = 1
for i in range(1, 4+1):
  fact *= i
print(fact)
