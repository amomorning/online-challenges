#include <bits/stdc++.h>
const int N = 5e5+10;

int a[N], c[N];

int sum(int i) {
	if(i == 0) return 1;
	int ret = 0;
	for(; i > 0; i -= i&-i) ret += c[i];
	return ret;
}

void add(int i, int x) {
	for(; i <= N; i += i&-i) c[i] += x;
}

int main() {
	int n, k, d; scanf("%d%d%d", &n, &k, &d);
	for(int i = 1; i <= n; ++ i) {
		scanf("%d", &a[i]);
	} 
	std::sort(a+1, a+n+1);
	for(int i = 1; i <= n; ++ i) if(sum(i-1)){
		// printf("%d\n", i);
		int r = std::upper_bound(a+1, a+n+1, a[i]+d) - a;
		int l = i+k-1;
		if(l < r) {
			add(l, 1);
			add(r, -1);
		}	
	}
	// }
	// puts("");
	if(sum(n)) puts("YES");
	else puts("NO");
}
