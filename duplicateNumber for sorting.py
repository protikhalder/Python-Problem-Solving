#TODO duplicate value index(0,1)

# list = [10,9,15,18,7,20,12,16,9,7]
# print(sorted(list))

# TODO duplicate value ay method kaz kora nh
# for i in range(len(list)):
#     min_value = min(list[i:])
#     min_index = list.index(min_value)
#     list[i], list[min_index] = list[min_index], list[i]
# print(list)



# 0th index min_value put ON
# 1th index min_value put ON
# 2th index min_value put ON
# 3th index min_value put ON
# 4th index min_value put ON
# list = [10,9,15,18,7,20,12,16,9,7]
# for i in range(len(list)):
#     min_value = min(list[i:])
#     min_index = list.index(min_value,i)
#     list[i], list[min_index] = list[min_index], list[i]
# print(list)

# Amaxlist = [10,9,15,18,7,20,12,16,9,7]
#
# for i in range(len(Amaxlist)):
#     max_value = max(Amaxlist[i:])
#     max_index =Amaxlist.index(max_value,i)
#     Amaxlist[i], Amaxlist[max_index] = Amaxlist[max_index] , Amaxlist[i]
# print(Amaxlist)

# lists = [10,9,15,18,7,20,12,16]
#
# for i in range(len(lists)-1):
#     min_value = min(lists[i:])
#     min_index = lists.index(min_value)
#     lists[i], lists[min_index] = lists[min_index], lists[i]
#     print(lists)


# TODO: both value differnt swaping some case index are same positon
lists = [10,9,15,18,7,20,12,16,9,7]

for i in range(len(lists)-1):
    max_value = max(lists[i:])
    max_index = lists.index(max_value,i)
    if lists[i] != lists[max_index]:
        lists[i], lists[max_index] = lists[max_index], lists[i]
print(lists)



