// "Copyright [2021] MeEk_0"
// problem form : https://codeforces.com/problemset/problem/228/A

#include<iostream>
#include <algorithm>

int main() {
    int i, j, count = 0, inputs[20];
    for (i = 0; i < 4; i++) {
        std::cin >> inputs[i];
    }
    std::sort(inputs, inputs+4);   // For not using another boring for loop, +4 is used because HE can only effort 4 shoes !
    for (i = 0; inputs[i]; i++) {
            if (inputs[i] == inputs[i+1]) {
                count = count + 1;
        }
    }
    std::cout << count << std::endl;
    return 0;
}
