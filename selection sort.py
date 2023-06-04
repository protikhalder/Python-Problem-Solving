# lists= [10,9,15,18,7,20,12,16,9,7]
# TODO: for selection sort 1 max value or 1 min value nao thn sorting and compareing and sort
# for i in range(len(lists)-1):
#     m_value = min(lists[i:])
# # TODO: (duplicate value index(0,i for 2nd index menas again fast thaka check korba))

#     m_index = lists.index(m_value, i)
#     if lists[i] != lists[m_index]:
#         lists[i], lists[m_index] = lists[m_index] , lists[i]
# print(lists)


# TODO: list min value and index
# for i in range(len(lists)-1):
#     m_value = lists[i]
#     for j in range(i+1, len(lists)):
#         if lists[j] < m_value:
#             m_value = lists[j]
#     m_index = lists.index(m_value, i)
#     if lists[i] != lists[m_index]:
#         lists[i] , lists[m_index] = lists[m_index], lists[i]
# print(lists)
# TODO: list MAX value and index

# for i in range(len(lists)-1):
#     max_value = lists[i]
#     for j in range(i+1, len(lists)):
#         if lists[j]>max_value:
#             max_value = lists[j]
#     max_index = lists.index(max_value, i)
#     if lists[i]!=lists[max_index]:
#         lists[i] , lists[max_index] = lists[max_index] , lists[i]
# print(lists)







# TODO: find out Index of minimum value

numbers = int(input("ENter nmuber"))


lists =[int(input()) for x in range(numbers)] #Python List Comparison

for i in range(len(lists)-1):
    max_index = i
    for j in range(i+1, len(lists)):
        if lists[j]> lists[max_index]:
            max_index = j
    if lists[i] != lists[max_index]:
        lists[i], lists[max_index] = lists[max_index], lists[i]
print(lists)


