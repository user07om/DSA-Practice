str_is = "hello world!"

vo = "aeiou"
dum = ""
slow = 0
for fast in range(len(str_is)):
    if str_is[fast] not in vo:
        print("Hello")
        #str_is[fast].join(dum)
        dum.join(str_is[fast])


print(dum)

