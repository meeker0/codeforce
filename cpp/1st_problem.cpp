// problem link :   https://codeforces.com/problemset/problem/231/A

#include<iostream>
#include <algorithm>
#include<cstring>



int main() {
    int n, i, success = 0;
    std::cin >> n;
    for (i=0; i <= n; i++) {
        std::string values;
        getline(std::cin, values, '\n');
        // for finding '1' in the string
        size_t count = std::count_if( values.begin(), values.end(), []( char c ){return c =='1';});
        // it's a lambda function
        if (count >= 2) {
            success++;
        }
    }
    std::cout << success << std::endl;
    return 0;
}
