"""画图"""
# import turtle
# from turtle import *
# import turtle as t
# t.pensize(2)
# for i in range(8):
#     t.fd(150)
#     t.left(135)
# turtle.done()
"""计算m到n的累加和"""
# m,n=eval(input())
# sum = 0
# for i in range(0,n+1):
#     sum = sum + m + i
#     if(m + i == n):
#         break
# print("sum={}".format(sum))
"""星号三角形"""
# N = int(input())
# for i in range(1,N + 1,2):
#     for j in range(,-1,-1):
#         print(" " * j,end="")
#         break
#     print("*" * i)
#     if (i == N):
#         break

# n = eval(input())
# for i in range(1,n+1,2):
#     print("{0:^{1}}".format('*'*i, n))
"""C3 恺撒密码之加密"""
P = input()
C =""
for s in P:
    if(ord(s)>=65 and ord(s)<=90):
        C += chr(ord('A')+((ord(s)-ord('A')+3)%26))
    elif(ord(s)>=97 and ord(s)<=122):
        C += chr(ord('a')+((ord(s)-ord('a') +3)%26))
    else:
        C += s
print(C)
