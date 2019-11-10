#include <bits/stdc++.h>
const int N = 1e3+10;

int a[N];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n, m; scanf("%d%d", &n, &m);
		for(int i = 0; i < n; ++ i) {
			scanf("%d", &a[i]);
		}
		int t = 0;
		while(a[t] == -1) {
			t ++;
		}
		for(int i = t+1; i < n; ++ i) {
			if(a[i] == -1) a[i] = (a[i-1]+1)%m;
		}
		for(int i = t-1; i >= 0; -- i) {
			a[i] = a[i+1]-1;
			if(a[i] < 0) a[i] += m;
		}
		for(int i = 0; i < n; ++ i) {
			printf("%d%c", a[i], " \n"[i+1 == n]);
		}
	}
}

