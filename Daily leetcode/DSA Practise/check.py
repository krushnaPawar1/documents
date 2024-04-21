#Subset SUM Problem
# def func(s,n):
#     t=[[0 for i in range(n+1)] for j in range(len(s)+1)]
#     # t=[[0]*(n+1)]*(len(s)+1)
#     for i in range(len(s)+1):
#
#         for j in range(n+1):
#             if i==0:
#                 t[i][j]=0
#             if j==0:
#                 t[i][j]=1
#     for i in range(1,len(s)+1):
#         for j in range(n+1):
#             if s[i-1]<=j:
#                 t[i][j]=(t[i-1][j-s[i-1]]) or t[i-1][j]
#             else:
#                 t[i][j]=t[i-1][j]
#     return t[len(s)][n]
#
#
# s=[2,6,1,9,5]
# n=98
# print(func(s,n))



# code for the equal partition
# You have given an array with size n you have to check that can we form the array in two two equal parts such that its sum are equal

# def partition(arr,n):
#     s=sum(arr)
#     if s%2!=0:
#         return False
#     else:
#         return func(arr,int(s/2))

# arr=[2,6,2]
# n=len(arr)
# print(partition(arr,n))




# Code for the finding the number of subset with the given sum


# def count(arr,n):
#     t=[[0 for i in range(sum(arr))] for j in range(n+1)]
#     for i in range(len(arr)+1):
#         for j in range(n+1):
#             if i==0:
#                 t[i][j]=0
#             if j==0:
#                 t[i][j]=1
#     for i in range(1,len(arr)+1):
#         for j in range(n+1):
#             if arr[i-1]<=j:
#                 t[i][j]=t[i-1][j-arr[i-1]] +t[i-1][j]
#             else:
#                 t[i][j]=t[i-1][j]
#     return t[len(arr)][n]
# arr=[1,4,2,5,6]
# n=6
# print(count(arr,n))



#code for the activity  selection problem using greedy algorithms
#
#
# s=[12,15,20]
# e=[11,20,25]
# l=[]
# for i in range(len(s)):
#     l.append([s[i],e[i]])
# l.sort(key=lambda x:x[1])
# c=1
# i=0
# for j in range(1,len(s)):
#     if l[j][0]>l[i][1]:
#         c+=1
#         i=j
# print(c)