# problem form : https://codeforces.com/problemset/problem/214/A

# from sympy import *

# x,y = symbols("x,y", intiger = True)

# m,n = input().split(' ')
# print(f'{int(m) , int(n)}')
# # solX = roots((x+(int(n)-x**2)**2 - int(m)), x)
# # solY = roots((int(m) - y**2)**2 + y - int(n), y)
# sol = solve([x**2 + y - int(n), y**2 + x - int(m)], [x, y])
# # print(f"{solX}  \n\n\n\n {solY}")
# print(sol)

# UnCool Version
count = 0
i = 0
m,n = input().split(' ')
big = m if int(m) > int(n) else n
while(i <= int(big)):
    for j in range(int(big)+1):
        if (((i**2)+ j) == int(n)) and ((i+j**2) == int(m)):
            count = count+1
    i = i+1
print(count)
