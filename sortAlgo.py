# TODO: Sort build-in-method of List
# TODO: Number sort ascending order

# num = [10,2,3.4,56,111, 567,89,9]
# num.sort()
# print(num)
# output: [2, 3.4, 9, 10, 56, 89, 111, 567]

# TODO: Number sort DEscending order
#
# num = [10,2,3.4,56,111, 567,89,9]
# num.sort(reverse=True)
# print(num)
# output: [567, 111, 89, 56, 10, 9, 3.4, 2]

# TODO: String or word sort DEscending order
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# letters.sort(reverse=True)
# print(letters)
# output: ['g', 'f', 'e', 'd', 'c', 'b', 'a']

# TODO: denpending on len thn list sorting

# list = ["cc", "b", "aaa","eeee", "fffffff"]
#
# list.sort(key=len)
# print(list)
# output: ['b', 'cc', 'aaa', 'eeee', 'fffffff']
# TODO: nested list sort processing
# list3=[[2,9], [1,10],[3,7]]
# list3.sort()
# print(list3)
# # [[1, 10], [2, 9], [3, 7]] #But 2nd value not sorted
#
# def SorybySecond(element):
#     return element[1]
# list3.sort(key=SorybySecond)
# print(list3)
# [[3, 7], [2, 9], [1, 10]] # Now sconed value is sorted