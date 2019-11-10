#include <bits/stdc++.h>
const int M = 1e3+10;

int a[M];

int main() {
	int n, w; scanf("%d%d", &n, &w);
	for(int i = 0; i < n; ++ i) scanf("%d", &a[i]);
	int min = 0;
	int max = w;
	bool f = 1;
	int cur = 0;
	for(int i = 0; i < n; ++ i) {
		cur += a[i];
		if(cur < 0) min = std::max(min, -cur);
		else if(cur <= w) max = std::min(max, w-cur);
		else f = 0;
	}	
	if(f && min <= max) printf("%d\n", max-min+1);
	else printf("0\n");
}
