"""斐波那契数列"""
# # 请在...补充一行或多行代码
# def fbi(n):
#     if n == 1 or n == 2:
#         return 1
#     elif n > 2:
#         return fbi(n-1) + fbi(n-2)
# n = eval(input())
# print(fbi(n))
"""汉诺塔"""
steps = 0
def hanoi(src, des, mid, n):
    global steps
    if n == 1:
        ...
        print("[STEP{:>4}] {}->{}".format(steps, src, des))
    else:
        ...

N = eval(input())
hanoi("A", "C", "B", N)