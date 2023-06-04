# min method use korta pare
#
# or
#TODO LEFT SIDE (main value) = minvalue
#1111 TOOK(thinking) a 1st value minimum value-
# if True 3<5:
#     chage minimul vaule
# if False 15<5:
#     do nothing
# 2222 the swap the smallest number to 0th index


#TODO : list swaping method 1 time swaping for index

# lists = [10,9,15,18,7,20,12,16]
# min_valu = min(lists) #found value
# # print(min_valu )
# min_index = lists.index(min_valu)#found index
# # print(min_index )
# lists[0], lists[min_index] = lists[min_index], lists[0] #swaping
# print(lists)

#
# temp = lists[0] #swaping
# lists[0] = lists[min_index] #swaping
# lists[min_index] = temp #swaping
#TODO : list swaping method 1 time swaping for index

# lists = [89,76,54,3,2,1]
# min_value = min(lists)
# min_index = lists.index(min_value)
# lists[0] , lists[min_index] = lists[min_index], lists[0]
# print(lists)
#TODO : list for loop index  min value

# lists = [89,76,54,3,2,1]
# print(sorted(lists, reverse=True))

# for i in range(len(lists)):
#     min_value = min(lists[i:])
#     min_index = lists.index( min_value)
#     lists[i] , lists[min_index ] =lists[min_index ] , lists[i]
# print(lists)
#TODO : list for loop index  max value
lists = [10,9,15,18,7,20,12,16]
for i in range(len(lists)):
    max_value = max(lists[i:])
    max_index = lists.index( max_value)
    lists[i], lists[ max_index ] = lists[ max_index ], lists[i]
print("max value", lists)