
 # rod cutting problem



#
# def cut(arr,n):
#     w=[i+1 for i in range(n)]
#     t=[[0 for i in range(n+1)] for j in range(n+1)]
#     for i in range(n+1):
#         for j in range(n+1):
#             if i==0 or j==0:
#                 t[i][j]=0
#             elif w[i-1]<=j:
#                 t[i][j]=max((arr[i-1]+t[i][j-w[i-1]]),t[i-1][j])
#             else:
#                 t[i][j]=t[i-1][j]
#     return t[n][n]
# n=8
# arr=[1,5,8,9,10,17,17,20]
# print(cut(arr, n))






# class Solution:
#     def cutRod(self, price, n):
#         w=[i+1 for i in range(n)]
#         t=[[0 for i in range(n+1)] for j in range(n+1)]
#         for i in range(n+1):
#             for j in range(n+1):
#                 if i==0 or j==0:
#                     t[i][j]=0
#                 elif w[i-1]<=j:
#                     t[i][j]=max((price[i-1]+t[i][j-w[i-1]]),t[i-1][j])
#                 else:
#                     t[i][j]=t[i-1][j]
#         return t[n][n]


# n=int(input())
# arr=map(int,input().split())





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
#                 t[i][j]=t[i][j-arr[i-1]] +t[i-1][j]
#             else:
#                 t[i][j]=t[i-1][j]
#     return t[len(arr)][n]
# arr=[3,2,5,6]
# n=10
#

#Max coin Exchange problem in python


# you have given a sum and some coins you have to find the maximum count of the coins which give sum
#
# def fun(s,n,arr):
#     t=[[0 for i in range(s+1)] for j in range(n+1)]
#     for i in range(n+1):
#         for j in range(s+1):
#             if i==0:
#                 t[i][j]=0
#             if j==0:
#                 t[i][j]=1
#
#     for i in range(1,n+1):
#         for j in range(s+1):
#             if arr[i-1]<=j:
#                 t[i][j]=t[i][j-arr[i-1]]+t[i-1][j]
#             else:
#                 t[i][j]=t[i-1][j]
#     return t[n][s]
#
#
# s=4
# n=3
# arr=[1,2,3]
# print(fun(s,n,arr))
