#include <bits/stdc++.h>

int main() {
	int n; scanf("%d", &n);
	printf("1 ");
	for(int i = 2; i*i < n; i ++) {
		if(n%i == 0) {
			while(n%i == 0) n /= i;
			printf("%d ", i);
		}
	}	
	
}
