# problem form : https://codeforces.com/problemset/problem/214/A

from sympy import *

#  the other values were <sympy.core.add.Add> type. So, I just defined a function to filterOUT these specific types from my list.
def rem(_list):
    return list(filter(lambda v: type(v) != Add, _list))

def no_Loop(input):
    x,y = symbols("x,y", intiger = True, negative =False)
    output = []
    m,n = input.split(' ')

    # I need to solve these 2 equations seperately. Otherwise, my defined function will not work without loop.
    solX = rem(solve((x+(int(n)-x**2)**2 - int(m)), x))
    solY = rem(solve((int(m) - y**2)**2 + y - int(n), y))

    if len(solX) == 0 or len(solY) == 0:
        print(0)
    else:
        output.extend(solX)      # using "Extend" to add multiple values in the list.
        output.extend(solY)
        print(int((len(output))/2))  # Obviously, result will come in pairs. So, I need to divide the length of the list by 2.

def Loop(input):
    count = 0
    i = 0
    m,n = input.split(' ')
    big = m if int(m) > int(n) else n
    while(i <= int(big)):
        for j in range(int(big)+1):
            if (((i**2)+ j) == int(n)) and ((i+j**2) == int(m)):
                count = count+1
        i = i+1
    print(count)

if __name__ == '__main__':
    noLoop(input())
    # Loop(input())
