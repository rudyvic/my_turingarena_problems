int res[3];

int find_sum(int* array, int n, int sum) {
    int temp_sum = 0;
    for(int i=0; i<n; i++) {
        for(int j=1; j<n; j++) {
            for(int k=2; k<n; k++) {
                temp_sum = array[i] + array[j] + array[k];
                if(sum==temp_sum) {
                    res[0] = i;
                    res[1] = j;
                    res[2] = k;
                    return 1;
                }
            }
        }
    }
    return 0;
}

int get_result(int i) {
    return res[i];
}
