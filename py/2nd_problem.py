# problem form : https://codeforces.com/problemset/problem/228/A

input = input().split(" ")
update = len(list(dict.fromkeys(input)))        # Dictionary can't have duplicate keyWords !
if update != len(input):
    print(len(input)-update)
else:
    print("0")
