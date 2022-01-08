// "Copyright [2021] MeEk_0"
// problem form : https://codeforces.com/problemset/problem/233/A

#include<iostream>

int main() {
    int n, i, update[100];
    std::cin >> n;
    if ((1< n <=100) && (n%2 == 0)) {
        for (i = 0; i <= n; i++) {
            if ((i > 0) && (i%2 == 0)) {
                update[i-1] = i;        // That's how even number will be placed before odd number
                std::cout << update[i-1] << " " << update[i] << " ";
                // For printing the elements of the array from index 1 to n
               //
            } else if ((i > 0) && (i%2 != 0)) {
                update[i+1] = i;     // That's how odd number will be placed after even number
            }
        }
    } else {
        std::cout << "-1" << std::endl;
    }
    return 0;
}
