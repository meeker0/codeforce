# problem form : https://codeforces.com/problemset/problem/236/A

input = input()
update = len(list(dict.fromkeys(input)))        # Dictionary can't have duplicate keyWords !
if (update%2 == 0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
