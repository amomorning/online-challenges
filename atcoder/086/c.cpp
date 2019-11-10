#include <bits/stdc++.h>
const int M = 1e5+10;
int t[M], x[M], y[M];

int main() {
	int n;
	scanf("%d", &n);
	x[0] = 0, y[0] = 0, t[0] = 0;
	for(int i = 1; i <= n; ++ i) {
		scanf("%d%d%d", &t[i], &x[i], &y[i]);
	}
	bool flag = true;
	for(int i = 1; i <= n; ++ i) {
        int tt = t[i] - t[i-1];
		int dis = abs(x[i]-x[i-1]) + abs(y[i]-y[i-1]);
		// printf("%d %d\n", dis, t[i]);
		if(dis > tt) flag = false;
		else if((tt-dis)%2) flag = false;
	}
	if(flag) puts("Yes");
	else puts("No");
}
