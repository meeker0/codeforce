problems = input()
count = 0
for i in range(int(problems)):
    soln = input().split(" ")
    one = soln.index('1')
    print(soln)
    print(one)
    if (len(one) >= 2):
        count+= count
    print(count)
