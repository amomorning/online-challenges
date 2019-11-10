#include <bits/stdc++.h>
const int M = 2e5+10;
int a[M], sum[M];

int main() {
	int n, k; scanf("%d%d", &n, &k);
	for(int i = 0; i < n; ++ i) scanf("%d", &a[i]);
	for(int i = n; i < n + k; ++ i) a[i] = a[i-n];
	for(int i = k; i < n + k; ++ i) {
		sum[i] = sum[i-k] + a[i];
	}	
	int ans = k;
	for(int i = k; i < k+k; ++ i) {
		if(sum[ans] > sum[i]) ans = i;
	}
	printf("%d\n", ans-k+1);
}
