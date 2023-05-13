# def fact(n):
#     x = 1
#     for i in range(1,n+1):
#         x *= i
#     return x
# def cmn(n,m):
#     if n == m:
#         return 1
#     elif n<m:
#         n ,m=m ,n
#         return int(fact(n)/(fact(m)*fact(n-m)))
#     else:
#         return int(fact(n)/(fact(m)*fact(n-m)))
# a,b=eval(input())
# print(cmn(a,b)) #此处编写调用上述函数进行实际计算的调用代码

def isPrime(n):
    if (n <= 1):
        return "False"
    elif (n == 2):
        return "True"
    for value in range(2, n):
        if (n % value == 0):
            return "False"
    else:
        return "True"
print(isPrime(eval(input())))