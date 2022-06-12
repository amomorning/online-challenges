#include <bits/stdc++.h>
int a[110];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n;
		double m;
		scanf("%d%lf", &n, &m);
		int cnt = 0;
		for(int i = 0; i < n; ++ i) {
			scanf("%d", &a[i]);
			if(a[i] >= 50) cnt ++;
		}
		if(cnt >= (int)ceil(m*n)) puts("YES");
		else puts("NO");
	}
}
