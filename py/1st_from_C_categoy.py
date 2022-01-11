# problem form : https://codeforces.com/problemset/problem/1374/C


for s in[*open(0)][2::2]:       # This will make the console input buffer as a list and seperated when \n is found
                                # [2::2] means [start_pos : end_pos : jump_value]
    while'()'in s:s=s.replace('()','')    # This will remove the nested brackets inside
    print(len(s)//2)    # Because the unpared brakets remain will be same in number.
