# code for the finding the length of the longest common subsequence from the gicen two strings


# There are various approach are there for the finding the lonsegt common subsquence such as 1.Recursion 2.Memoisization and dynamic programing


# RECURSIVE APPROACH
# def lcs(x,y,n,m):
#     if n==0 or m==0:
#         return 0
#     elif x[n-1]==y[m-1]:
#         return (1+lcs(x,y,n-1,m-1))
#     else:
#         return max(lcs(x,y,n,m-1),
#                    lcs(x,y,n-1,m))



# MEMOMISATION Bottom up approach

# def lcs(x,y,m,n):
#     dp=[[-1 for i in range(n+1)] for j in range(m+1)]
#     if m==0 or n==0:
#         return 0
#     if dp[m][n] !=-1:
#         dp[m][n]=-1
#     elif x[m-1]==y[n-1]:
#         dp[m][n]=1+lcs(x,y,m-1,n-1)
#         return dp[m][n]
#     else:
#         dp[m][n]=max(lcs(x,y,m,n-1),lcs(x,y,m-1,n))
#         return dp[m][n]
# x= "AGGTAB"
# y ="GXTXAYB"
#
# print(lcs(x,y,len(x),len(y)))

# TOP DOWN APPROACH in DP




# def lcs(x,y,m,n):
#     t=[[0 for i in range(n+1)] for j in range(m+1)]
#     for i in range(m+1):
#         for j in range(n+1):
#             if i==0 or j==0:
#                 t[i][j]=0
#             elif x[i-1]==y[j-1]:
#                 t[i][j]=t[i-1][j-1]+1
#             else:
#                 t[i][j]=max(t[i-1][j],t[i][j-1])
#     return t[m][n]
#
# x= "AGGTAB"
# y ="GXTXAYB"
#
# print(lcs(x,y,len(x),len(y)))




# code for the finding the longest common substring in python
# def longestcommonsubstrin(x,y,m,n):
#     t=[[0 for i in range(n+1)] for j in range(m+1)]
#     res=0
#     for i in range(m+1):
#         for j in range(n+1):
#             if i==0 or j==0:
#                 t[i][j]=0
#             elif x[i-1]==y[j-1]:
#                 t[i][j]=1+t[i-1][j-1]
#                 res=max(res,t[i][j])
#             else:
#                 t[i][j]=0
#     return res
# x= "AGGTAB"
# y ="GXTXAB"
# m=len(x)
# n=len(y)
# print(longestcommonsubstrin(x,y,m,n))


#Code for the printing the LCS


# def plcs(x,y,m,n):
#     t=[[0 for i in range(n+1)] for j in range(m+1)]
#     for i in range(m+1):
#         for j in range(n+1):
#             if i==0 or j==0:
#                 t[i][j]=0
#             elif x[i-1]==y[j-1]:
#                 t[i][j]=1+t[i-1][j-1]
#             else:
#                 t[i][j]=max(t[i-1][j],t[i][j-1])
#     res=""
#     while m>0 and n>0:
#         if x[m-1]==y[n-1]:
#             res+=x[m-1]
#             m-=1
#             n-=1
#         elif x[m-1]>y[n-1]:
#             m-=1
#         else:
#             n-=1
#     return res[::-1]
#
#
#
# x= "AGGTAB"
# y ="GXTXAB"
# m=len(x)
# n=len(y)
# print(plcs(x,y,m,n))


# shortest common supersequence




#
# def fun(x,y,m,n):
#     t=[[0 for i in range(n+1)] for j in range(m+1)]
#     for i in range(m+1):
#         for j in range(n+1):
#             if i==0 or j==0:
#                 t[i][j]=0
#             elif x[i-1]==y[j-1]:
#                 t[i][j]=1+t[i-1][j-1]
#             else:
#                 t[i][j]=max(t[i-1][j],t[i][j-1])
#     return m+n-t[m][n]
# x= "AGGTAB"
# y ="GXTXAB"
# m=len(x)
# n=len(y)
# print(fun(x,y,m,n))



# 25 Minimum Number of Insertion and Deletion to convert String a to String b

# def fun(x,y,m,n):
#     t=[[0 for i in range(n+1)] for j in range(m+1)]
#     for i in range(m+1):
#         for j in range(n+1):
#             if i==0 or j==0:
#                 t[i][j]=0
#             elif x[i-1]==y[j-1]:
#                 t[i][j]=1+t[i-1][j-1]
#             else:
#                 t[i][j]=max(t[i-1][j],t[i][j-1])
#     return m-t[m][n]+n-t[m][n]
# x= "AGGTAB"
# y ="GXTXAB"
# m=len(x)
# n=len(y)
# print(fun(x,y,m,n))



#code for the finding the longest palindromic subsequence

# def lps(a):
#     b=a[::-1]
#     n=len(a)
#     t=[[0 for i in range(n+1)] for j in range(n+1)]
#     for i in range(n+1):
#         for j in range(n+1):
#             if i==0 or j==0:
#                 t[i][j]=0
#             elif a[i-1]==b[j-1]:
#                 t[i][j]=1+t[i-1][j-1]
#             else:
#                 t[i][j]=max(t[i-1][j],t[i][j-1])
#     return t[n][n]
# a="agbcba"
# print(lps(a))



#code for the chcking the minimum number of insertion and the deletion operation for the making to make the palindrome

# s="aebcbda"
# def fun(s):
#     a=s
#     b=a[::-1]
#     n=len(a)
#     t=[[0 for i in range(n+1)] for j in range(n+1)]
#     for i in range(n+1):
#         for j in range(n+1):
#             if i==0 or j==0:
#                 t[i][j]=0
#             elif a[i-1]==b[j-1]:
#                 t[i][j]=1+t[i-1][j-1]
#             else:
#                 t[i][j]=max(t[i-1][j],t[i][j-1])
#     return n-t[n][n]
# print(fun(s))
#


#CODE FOR THE LONGEST REPEATING SUBSEQUENCE
#
# def lrs(s):
#     a=s
#     b=s
#     t=[[0 for i in range(len(a)+1)] for j in range(len(a)+1)]
#     for i in range(len(a)+1):
#         for j in range(len(a)+1):
#             if a[i-1]==b[i-1] and i!=j:
#                 t[i][j]=1+t[i-1][j-1]
#             else:
#                 t[i][j]=max(t[i-1][j],t[i][j-1])
#     return int(t[len(a)][len(a)]/2)
# s="abacdedab"
# print(lrs(s))

# code for the reversing the string in group

#
# s="abcdefg"
# k=2
# d1=""
# for i in range(0,len(s),k):
#     p=s[i:i+k]
#     d=p[::-1]
#     # print(d)
#     d1=d1+d
#
# print(d1)
