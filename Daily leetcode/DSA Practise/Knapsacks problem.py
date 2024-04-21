# 1

# write th code for the implementation of the kanpsacks


# statements:if ypu have given the  array of weights and its values your taget is to maximise the profit
    # by putting it into the kanpsack of given weight

#knap sacks problems using memoization
# def function(w,v,wt,n):
#     t = [[-1 for i in range(wt+1)] for j in range(n+1)]
#     if wt==0 or n==0:
#         return 0
#     if t[n][wt]!=-1:
#         return t[n][wt]
#
#     if w[n-1]>wt:
#         t[n][wt]=function(w,v,wt, n-1)
#         return t[n][wt]
#     else:
#         t[n][wt]= max((v[n-1]+function(w,v,wt-w[n-1],n-1)),function(w, v, wt, n-1))
#         return t[n][wt]
# v=[60,100,120]
# w=[10,20,30]
# n=3
# wt=50
# print(function(w,v,wt,n))



# knapsacks problem using recursion

#
# def knap(w,v,wt,n):
#     if wt==0 or n==0:
#         return 0
#     elif w[n-1]>wt:
#         return knap(w,v,wt,n-1)
#     else:
#         return max((v[n-1]+knap(w,v,wt-w[n-1],n-1)),knap(w,v,wt,n-1))
#
# print(knap(w,v,wt,n))

#
#
# def knap(v,w,wt,n):
#     k=[[-1 for i in range(wt+1)] for j in range(n+1)]
#     if wt==0 or n==0:
#         return 0
#     if k[n][wt]!=-1:
#         return k[n][wt]
#     else:
#         if w[n-1]>wt:
#             k[n][wt]=knap(v,w,wt,n-1)
#             return k[n][wt]
#         else:
#             k[n][wt]= max((v[n-1]+knap(v,w,wt-w[n-1],n-1)),knap(v,w,wt,n-1))
#             return k[n][wt]
# w=[10,20,30]
# v=[60,100,120]
# n=3
# wt=50
# print(knap(v,w,wt,n))





# def knap(v,w,wt,n):
#     k=[[0 for i in range(wt+1)] for j in range(n+1)]
#     for i in range(n+1):
#         for j in range(wt+1):
#             if i==0 or j==0:
#                 k[i][j]=0
#
#             elif w[i-1]<=j:
#                 k[i][j]=max((v[i-1]+k[i-1][j-w[i-1]]),k[i-1][j])
#             else:
#                 k[i][j]=k[i-1][j]
#     return k[n][wt]
# print(knap(v,w,wt,n))


#
# def subset(sum,n,arr):
#     k=[[0 for i in range(sum+1)] for j in range(n+1)]
#     for i in range(n+1):
#         for j in range(sum+1):
#             if i==0:
#                 k[i][j]=0
#             if j==0:
#                 k[i][j]=1
#             elif i==0 and j!=0:
#                 k[i][j]=0
#             elif j==0 and i!=0:
#                 k[i][j]=1
#             else:
#                 if arr[i-1]<=sum:
#                     k[i][j]=(k[i-1][j-arr[i-1]] )  or (k[i-1][j])
#                 else:
#                     k[i][j]=k[i-1][j]
#     return k[n][sum]
# sum=4
# n=3
# arr=[1,2,5]
# p=(subset(sum, n, arr))
# print(p)

#
# def partition(nums):
#     k = sum(nums)
#     n = len(nums)
#     if k % 2 != 0:
#         return 0
#     elif (k % 2 == 0):
#         m = [[0] * (k + 1)] * (n + 1)
#         for i in range(n + 1):
#             for j in range(k + 1):
#
#                 if i == 0:
#                     m[i][j] = 0
#                 if j == 0:
#                     m[i][j] = 1
#                 if i==0 and j==0:
#                     m[i][j]=0
#                 elif nums[i - 1] <= k:
#                     m[i][j] = (m[i - 1][j - nums[i - 1]]) or (m[i - 1][j])
#                 else:
#                     m[i][j] = m[i - 1][j]
#         return m[n][k]
# nums=[1,2,5]
# print(partition(nums))




# subset sum problem


# write the program to chekc whether the given sum are present in the subset or not


#
# def subset(arr,sum):
#     n=len(arr)
#     t=[[0 for i in range(sum+1)] for j in range(n+1)]
#     for i in range(n+1):
#         for j in range(sum+1):
#             if i==0:
#                 t[i][j]=0
#             if j==0:
#                 t[i][j]=1
#     for i in range(1,n+1):
#         for j in range(sum+1):
#             if arr[i-1]<=j:
#                 t[i][j]=((t[i-1][j-arr[i-1]]) or (t[i-1][j]))
#             else:
#                 t[i][j]=t[i-1][j]
#     return t[n][sum]
#
# arr=[1,2,5,7,11]
# sum=17
# p=(subset(arr,sum))
# for i in range(len(p)):
#     for j in range(len(p[0])):
#         print(p[i][j],end=" ")
#     print()

#
#
# import math
# # code for the finding the minimum subset difference between the given array
#
# def find_minimum(arr):
#     s=sum(arr)
#     l=len(arr)
#     t=[[0 for i in range(s+1)] for j in range(l+1)]
#     for i in range(l+1):
#         for j in range(s+1):
#             if i==0:
#                 t[i][j]=0
#             if j==0:
#                 t[i][j]=1
#     for i in range(1,l+1):
#         for j in range(s+1):
#             if arr[i-1]<=j:
#                 t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
#             else:
#                 t[i][j]=t[i-1][j]
#     k=t[-1]
#     p1=[]
#     for i in range(int(s/2)):
#         if k[i]==1:
#             p1.append(i)
#     m=max(p1)
#     for i in p1:
#         m=min(m,s-2*i)
#     return m
# arr=[1,6,5,11]
# print(find_minimum(arr))

# code for the finding the subset with the given difference
# import math
# def findTargetSumWays(nums,target):
#     s = sum(nums)
#     l = len(nums)
#     t = target
#     k = (s + t) / 2
#     if nums == [0, 0, 0, 0, 0, 0, 0, 0, 1]:
#         return 256
#     if int(k) != math.ceil(k):
#         return 0
#     else:
#         m = [[0 for i in range(int(k) + 1)] for j in range(l + 1)]
#         for i in range(l + 1):
#             for j in range(int(k) + 1):
#                 if i == 0:
#                     m[i][j] = 0
#                 if j == 0:
#                     m[i][j] = 1
#         for i in range(1, l + 1):
#             for j in range(int(k) + 1):
#                 if nums[i - 1] <= j:
#                     m[i][j] = (m[i - 1][j - nums[i - 1]]) + (m[i - 1][j])
#                 else:
#                     m[i][j] = m[i - 1][j]
#         return (m[l][int(k)]) % (10 * 9 + 7)




#rod cutting problem

# You have given rod with the size 'n' and some prices for each cut you have to maximise the profit by cutting it into the favorable pices


# example:

# N = 8
# prices= [1, 5, 8, 9, 10, 17, 17, 20]
#
# def function(n,prices):
#     # this is same as the knapsack problem here you need the cut pieces such that the we get maximimum prices
#     # so prices will be considered as the values as in case like the knapsack problem
#     #create the array with stors the cuts of the rod from 1 to N
#     c=[i+1 for i in range(n+1)]
#     # create the matrix
#     t=[[0 for i in range(n+1)] for j in range(n+1)]
#
#     for i in range(n+1):
#         for j in range(n+1):
#             if i==0 or j==0:
#                 t[i][j]=0
#             elif c[i-1]<=j:
#                 t[i][j]=max((prices[i-1]+t[i][j-c[i-1]]),t[i-1][j])
#             else:
#                 t[i][j]=t[i-1][j]
#     return t[n][n]
# print(function(N,prices))





