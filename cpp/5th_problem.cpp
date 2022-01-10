// "Copyright [2021] MeEk_0"
// problem form : https://codeforces.com/problemset/problem/233/A

#include<iostream>
#include<cmath>

int main() {
    int j, i, update[100], big, m, n, count = 0;
    for (i = 0; i < 2; i++) {
    std::cin >> update[i];
    }
    m = update[0];
    n = update[1];
    if (m > m) {
        big = m;
    } else {
        big = n;
    }
    for (i=0; i <= big; i++) {
        for (j=0; j<= big; j++) {
            if ((pow(i, 2)+ j == n) && (i+pow(j, 2) == m)) {
                count = count + 1;
            }
        }
    }
    std::cout << count;
    return 0;
}
