#include <vector>
#include <algorithm>

std::vector<int> res(3);

void find_sum(int n, int* a, int sum) {
    int temp_sum = 0;

    for(int i=0; i<n; i++) {
        for(int j=1; j<n; j++) {
            for(int k=2; k<n; k++) {
                temp_sum = a[i] + a[j] + a[k];
                if(sum==temp_sum) {
                    res[0] = i;
                    res[1] = j;
                    res[2] = k;
                    return;
                }
            }
        }
    }
}

int get_result(int i) {
    return res[i];
}

