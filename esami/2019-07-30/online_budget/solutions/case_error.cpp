#include <vector>
#include <algorithm>

std::vector<int> b;

void sort(int n, int* a) {
    b = {a, a+n};
    std::sort(b.begin(), b.end());
}

/* Errore nel momento in cui la dimensione dell'input è grande */
int distinct(int n){

	if(n <= 100 || n > 1000){
		int count = 0;

		for(int i = 0; i < n - 1; i++)
			if(b[i] != b[i+1])
				count++;

		return count == 0 ? count : ++count;
	}
	else
		return 0;
}


