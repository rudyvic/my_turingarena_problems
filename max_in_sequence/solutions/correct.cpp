int compare_two_arrays(int n, int* a, int* b) {
    for(int i = 0; i < n; i++)
        if(a[i] != b[i])
            return i;
    return -1;
}
