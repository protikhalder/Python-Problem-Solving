# TODO: n of elemet compare eash pair item adjaect and swap

# lists= [10,9,15,18,7,20,12,16,9,7]
# lists=[10,15,4,23,0]

# num = int(input("Loop you want"))
# lists = [int(input()) for x in range(num)]
# for j in range(len(lists)-1):
#     for i in range(len(lists)-1-j):
#         if lists[i]>lists[i+1]:
#             lists[i], lists[i+1]= lists[i+1], lists[i]
#             print(lists)
#         else:
#             print(lists)
#     print()
# print(lists)

num = int(input("loop uoy want: "))
lists = [int(input()) for x in range(num)]

for i in range(len(lists)-1,0,-1):
    for j in range(i):
        if lists[j] > lists[j+1]:
            lists[j] ,lists[j+1] = lists[j+1],  lists[j]
print(lists)