# TODO: Direct
# def natural (n):
#     while(n==0):
#         return
#     print(n,end=" ")
#     natural(n-1)
# natural(10)


# def natural(n):
#     if(n>=0):
#         if(n==0):
#             return
#     print(n, end=" ")
#     natural(n-1)
# natural(10)

# def natural(n):
#     if(n<=0):
#         return
#     print(n,end=" ")
#     natural(n-1)
# natural(40)

# TODO: indirect
# def natural(n):
#     if n<=0:
#         return
#     print(n, end=" ")
#     natural1(n-1)
# def natural1(n):
#     print(n, end=" ")
#     natural(n-1)
# natural(10)

#TODO: Print First uppercase letter in a string Using Recursion

# def first_upper(str,i):
#     l = len(str)
#     if i>=l:
#         return -1
#     if str[i].isupper():
#         return i
#     if i<l:
#         return first_upper(str,i+1)
# str = input("Enter anny: ")
# index = first_upper(str,0) #this function all time return me i(index)
# if(index!=-1):
#     print("Found char =", str[index])
# else:
#     print("not found")

# def first_upper(pop,i):
#     l = len(pop)
#     if i>=l:
#         return -1
#     if pop[i].isupper():
#         return pop[i]
#     if i<l:
#         return first_upper(pop,i+1)
# pop = input("Ente: ")
# index = first_upper(pop,0)
# if (index!=-1):
#     print("Found Char= ",index)
# else:
#     print("Nikdv")



# def maxValue(lists, l, maximum):
#     if l == 0:
#         return maximum
#     if l>0:
#         if lists[l]>maximum:
#             maximum=lists[l]
#     return maxValue(lists, l-1, maximum)
#
#
# lists = [10,9,15,18,7,20,12,16]
# l=len(lists)-1
# maxmum = lists[0]
# print(maxValue(lists,l,maxmum))

# def minmumVAlue(a, l, minimum):
#     if l == 0:
#         return minimum
#     if l>0:
#         if a[l]<minimum:
#             minimum=a[l]
#     return minmumVAlue(a, l-1, minimum)
#
#
# a = [10,9,15,18,7,20,12,16]
# l=len(a)-1
# minimum= a[0]
#
# print(minmumVAlue(a,l,minimum))

#
# TODO:Happy number and unhappy number
# num1 = int(input("Entr num1: "))
# num2 = int(input("Enter num2: "))
#
# while(num1<num2):
#     sum = 0
#     temp = num1
#     while sum!=1 and sum!=4:
#         sum=0
#         while temp!=0:
#             rem = int(temp%10)
#             sum = sum+rem*rem
#             temp=(temp/10)
#         temp = sum
# 
#     if sum == 1:
#         print("Happy value")
#     else:
#         print("Unhappy value")
#     num1=num1+1

# num1 = int(input("Entr num1: "))
# num2 = int(input("Enter num2: "))
#
# while(num1<num2):
#     sum = 0
#     temp = num1
#     if (sum==1):
#         print("happy Number")
#     num1=num1+1


def maxValue(lists, l, maximun):
    if l == 0:
        return maximun
    if l>0:
        if lists[l] > maximun:
            maximun =lists[l]
    return maxValue(lists, l-1, maximun)

lists = [10,9,15,18,7,20,12,16,9,7]
maximun = lists[0]
l = len(lists)-1

print(maxValue(lists,l,maximun))