# matrix chain multipication
# import sys
# def fun(arr,i,j):
#     if i>=j:
#         return 0
#     m=sys.maxsize
#     for k in range(i,j):
#         m=min(m,fun(arr, i, k)+fun(arr,k+1,j)+arr[i-1]*arr[k]*arr[j])
#     return m
#
#
# n=5
# arr=[40,30,20,50,10]
# i=1
# j=n-1
# k=fun(arr,i,j)
# print(k)



# memoization code for mcm
# global t
#
# import sys
# def fun(arr,i,j):
#     if t[i][j]!=-1:
#         return t[i][j]
#     if i>=j:
#         return 0
#     m=sys.maxsize
#     for k in range(i,j):
#         m=min(m,fun(arr, i, k)+fun(arr,k+1,j)+arr[i-1]*arr[k]*arr[j])
#     t[i][j]=m
#     return t[i][j]
#
#
# n=5
# arr=[40,30,20,50,10]
# i=1
# j=n-1
# t=[[-1]*(n+1)]*(n+1)
# k=fun(arr,i,j)
#
# print(k)
#


# CODE FOR THE PALINDROME PARTITIONING
# import sys
# def palindrome(string,i,j):
#     if i==j:
#         return True
#     if i>j:
#         return True
#     else:
#         while i<j:
#             if string[i]!=string[j]:
#                 return False
#             else:
#                 i+=1
#                 j-=1
#         return True
#
# def function(s,i,j):
#     if i>=j:
#         return 0
#     if palindrome(s,i,j)==True:
#         return 0
#     m=sys.maxsize
#     for k in range(i,j):
#         m=min(m,1+ function(s,i,k)+function(s,k+i,j))
#     return m
#
# s="ababbbabbababa"
# i=0
# j=len(s)-1
# print(function(s,i,j))


#
# import sys
# def ispalindrome(s):
#     return s == s[::-1]
#
# def palindromicPartition(string):
#     def solve(string, i, j):
#         if i>=j or ispalindrome(string[i:j + 1]):
#             return 0
#         m = sys.maxsize
#         for k in range(i, j - 1):
#             rm = 1 + solve(string, i, k) + solve(string, k + 1, j)
#             m = min(rm, m)
#         return m
#
#     i = 0
#     j = len(string) - 1
#     return solve(string, i, j)
#
#
# a="geeks"
# print(palindromicPartition(a))