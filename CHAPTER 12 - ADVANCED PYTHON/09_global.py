a = 89
def fun():
    #global a
    a = 3
    print(a)


print(a)
fun()    #OUTPUT: 89 AND THEN 3

# fun()
# print(a)    #OUTPUT: 3 AND THEN 89

#IF GLOBAL WORD IS ADDED IN FUN()
# fun()
# print(a)     #OUTPUT: 3 AND THEN ALSO 3