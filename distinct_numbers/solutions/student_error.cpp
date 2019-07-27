#include <vector>
#include <algorithm>

std::vector<int> b;

void sort(int n, int* a) {
    b = {a, a+n};
    std::sort(b.begin(), b.end());
}

int distinct(int n){
	int count = 0;

	for(int i = 0; i < n - 1; i++)
		if(b[i] != b[i+1])
			count++;

	// Tipico errore di uno studente potrebbe essere ritornare il contatore 
	// senza considerare che 1 confronto corrisponde a  2 numeri diversi
	return count;
}


