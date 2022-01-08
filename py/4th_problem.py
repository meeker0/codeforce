# problem form : https://codeforces.com/problemset/problem/233/A

update = []
input = int(input())
if (1< input <=100) and (input%2 == 0):
    for i in range(input+1):
        if (i>0 and i%2 == 0):
            update.insert(i-2,i)    # For even number before the odd number
        elif (i>0 and i%2 != 0):
            update.insert(i+1,i)
    print(*update, sep= ' ')        # Print the list without any brackets and commas
elif (input%2 != 0):
    print("-1")
