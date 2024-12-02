# ITP1_3_B
# i = 1
# while True:
#     num = int(input())  # 入力を受け取る
#     if num == 0:  # 終了条件
#         break
#     print(f"Case {i}: {num}")
#     i += 1

# 3-C
# while True:
#   a,b = map(int, input().split())
#   if a==0 and b==0:
#     break
#   if a > b:
#     print(b,a)
#   else:
#     print(a,b)

# 3-C 別解
# while True:
#   a,b = map(int, input().split())
#   if a==0 and b==0:
#     break
#   print(*sorted([a,b]))

# 3-D
# a,b,c = map(int, input().split())
# count = 0
# for i in range(a, b+1):
#   if c % i == 0:
#     count+=1
# print(count)

# 4-A
# a,b = map(int, input().split())
# d = a//b
# r = a%b
# f = a/b
# print(f"{d} {r} {f:.5f}")

# 4-B
# import math
# r = float(input())
# area = math.pi * r **2
# circum = 2 * r * math.pi
# print(f"{area:.6f} {circum:.6f}")

# 4-C
# while True:
#   a,op,b = input().split()
#   if op in "?":
#     break
#   a = int(a)
#   b = int(b)
#   if op == '+':
#       print(a + b)
#   elif op == '-':
#       print(a - b)
#   elif op == '*':
#       print(a * b)
#   elif op == '/':
#       print(a // b)

# 4-C 別解
# while True:
#     # strip()は空白を削除
#     line = input().strip()
#     if '?' in line:
#         break
#     # 入力を分割
#     a, op, b = line.split()
#     a = int(a)
#     b = int(b)
#     operations = {
#       '+': lambda x, y: x + y,
#       '-': lambda x, y: x - y,
#       '*': lambda x, y: x * y,
#       '/': lambda x, y: x // y,
#     }
#     if op in operations:
#       print(operations[op](a, b))
#     else:
#       print("無効な演算子です")

# 4-D
# num = int(input())
# lst = list(map(int, input().split()))
# min_val = min(lst)
# max_val = max(lst)
# sum_val = sum(lst)
# print(f"{min_val} {max_val} {sum_val}")

# 5-A
# while True:
#   h,w = map(int, input().split())
#   if h==0 and w==0:
#     break
#   for i in range(1, h+1):
#     for j in range(1, w+1):
#       print("#",end="")
#     print()
#   print()

# 5-A 別解
# while True:
#   h,w = map(int, input().split())
#   if h==0 and w==0:
#     break
#   for i in range(1, h+1):
#     print("#" * w)
#   print()

# 5-B
# while True:
#   h,w = map(int, input().split())
#   if h==0 and w==0:
#     break
#   for i in range(1, h+1):
#     print("#",end="")

#     if i==1 or i==h:
#       for j in range(2, w):
#         print("#",end="")
#     else:
#       for j in range(2, w):
#         print(".",end="")

#     print("#")
#   print()

# 5-C
# while True:
#   h,w = map(int, input().split())
#   if h==0 and w==0:
#     break
#   for i in range(1, h+1):
#     for j in range(1, w+1):
#       if i%2 == 1:
#         if j%2 == 1:
#           print("#",end="")
#         else:
#           print(".", end="")
#       else:
#         if j%2 == 0:
#           print("#",end="")
#         else:
#           print(".", end="")
#     print() 
#   print()
      