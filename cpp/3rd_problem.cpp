// "Copyright [2021] MeEk_0"
// problem form : https://codeforces.com/problemset/problem/236/A

#include<iostream>
#include <algorithm>    // For sorting
#include<cstring>   // For .size()

int main() {
    std::string name;
    std::cin >> name;
    //
    // Work around for removing duplicates
    std::sort(name.begin(), name.end());    // Sorting is important becuse of the technique bellow
    auto update = std::string(name.begin(), (unique(name.begin(), name.end())));
    //
    if (update.size()%2 == 0) {
        std::cout << "CHAT WITH HER!";
    } else {
        std::cout << "IGNORE HIM!";
    }
    return 0;
}
