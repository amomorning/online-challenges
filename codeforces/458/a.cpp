#include <bits/stdc++.h>

bool bad(int x) {
	if(x < 0) return true;
	if(x <= 1) return false;
	int t = sqrt(x);
	if(t*t == x || (t+1)*(t+1) == x) return false;
	return true;
}

int main() {
	int n;
	scanf("%d", &n);
	int ans = -1e6-7;
	for(int i = 0; i < n; i ++) {
		int x;
		scanf("%d", &x);
		if(bad(x)) ans = std::max(ans, x);
	}
	printf("%d\n", ans);
}
