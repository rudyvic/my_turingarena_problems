#include <vector>
#include <algorithm>

std::vector<int> b;

void reverse_array(int n, int* a) {
    b = {a, a+n};
    std::reverse(b.begin(), b.end());
}

int get_element(int i) {
    return b[i];
}
