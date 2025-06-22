myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item ** 2)
# print(squaredList) 

#THIS CAN BE DONE IN ONE LINE WITH A LIST COMPREHENSION:
squaredList = [i * i for i in myList]
print(squaredList)    