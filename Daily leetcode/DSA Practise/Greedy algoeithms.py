# Maximum event in the audotorium

#you have given the initial time of the events and its finishing time your task is to find the events such that the the max event are possible in the audotoium

#
# s=[12,10,20]
# f=[25,20,30]
# l=[]
# for i in range(len(s)):
#     l.append([s[i],f[i]])
# l.sort(key=lambda x:x[1])
# # [[10, 20], [12, 25], [20, 30]]
# i=0
# sel=[]
# for j in range(len(s)):
#     if l[j][0]>=l[i][1]:
#         i=j
#         sel.append(l[i])
# print(sel)
#




# job sequencing problem
#you are given the array which is filled with the jobs which mainly contain the jobid,job duration and the job pricing then you have to select a jobs in such a way that you have
#make maximum profit.
#
# l=[
#     [1,4,20],
#     [2,1,10],
#     [3,1,40],
#     [4,1,30]
# ]
# n=len(l)
# l.sort(key=lambda x:x[2],reverse=True)
#
#
# res=[False]*len(l)
# job=0
# sum=0
#
# for i in range(len(l)):
#     for j in range(min(len(l),l[i][1]),-1,-1):
#         if res[j] is False:
#             res[j]=True
#             job+=1
#             sum+=l[j][2]
#             break
# print(job)
# print(sum)



#knapsacks fractional problems


#you have given the values and thier weights and the maximum capacity of the knapsacks you need the add the weights into the knapasacks such that the
#profit will goes higher



# def fun(val,weight,n):
#     kf=[]
#     l=len(val)
#     n1=0
#     for i in range(l):
#         m=val[i]/weight[i]
#         kf.append([val[i],weight[i],m])
#     kf.sort(key=lambda x:x[2],reverse=True)
#     sum=0
#     for i in range(l):
#         if (kf[i][1])<=n:
#             sum+=kf[i][0]
#             n-=kf[i][1]
#         else:
#             su=(n*kf[i][2])
#             sum+=su
#             break
#     return(sum)
#
# n=10
# val=[500]
# weight=[30]
# print(fun(val,weight, n))




# choose and swap problem using greedy method

# for this problem the approach are simple you have to create the one dict which contain the element are visited or not initially set all the values to the NOne
#   After that you have to iterate over the letters and find the letters beloew from this place which arenot visited and simply do the replaement
#and in this wat we can get the lexographically sorted list




# def swapandchoose(s):
#     d={}
#     for i in s:
#         d[i]=True
#     for i in s:
#         for j in [chr(i) for i in range(ord('a'),ord(i))]:
#             if j in d and d[i]:
#                 s=s.replace(i,"*")
#                 s=s.replace(j,i)
#                 s=s.replace("*",j)
#                 return s
#         d[i]=False
#     return s
# s="ccad"
# print(swapandchoose(s))


#code for the minimum number of the platforms for train


# a=[1,2,6,8]
# d=[]

# n=5
# i=1
# c=0
# while i<=n:
#         c+=1
#         n-=i
#         i+=1
# print(c)

# from itertools import  combinations_with_replacement
# a="indiian"
# b="indian"
# if a==b:
#     print(0)
# else:
#     d=combinations_with_replacement(a,len(b))
#     h=0
#     for i in d:
#         if "".join(i)==b:
#             h+=1
#     print(h)



#
# n=int(input())
# m=str(n)
# if len(m)==1:
#     print("Enter the number which are greater than 9")
# else:
#     k=len(m)
#     c=0
#     while k>1:
#         c+=1
#         s=[int(i) for i in m]
#         p=sum(s)
#         m=str(p)
#         k=len(m)
#
#
#     print(c)


#code for the conversion of the given string into the 3 plindromic string


# s=input()
#
#
# l=len(s)
# for i in range(1,l-1):
#


# code for the invrds of dictionary
#
# d={
#     "a":10,
#     "b":20,
#     "c":30
# }
# m={}
# for i,j in d.items():
#     m[j]=i
# print(m)




