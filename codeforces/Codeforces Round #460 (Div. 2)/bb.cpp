#include <bits/stdc++.h>
const int M = 1e5+10;
int a[M];

int check(int x) {
	int cnt = 0;
	while(x) {
		cnt += x%10;
		x /= 10;
	}
	return cnt == 10;
}

int main() {
	int cnt = 0;
	for(int i = 0; i < 2e7; i ++) {
		if(check(i)) a[cnt++] = i;
	}
	int n; 
	scanf("%d", &n);
	printf("%d\n", a[n-1]);
}
