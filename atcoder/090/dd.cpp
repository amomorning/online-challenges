#include <bits/stdc++.h>
const int M = 1e5+10;
int d[M];

int main() {
	int n, m; scanf("%d%d", &n, &m);
	for(int i = 0; i < m; i ++) {
		
		int u, v, w; scanf("%d%d%d", &u, &v, &w);
		bool flag = true;
		if(!d[v]) d[v] = d[u] + w;
		else {
			if(d[v] != d[u] + w) flag = false;
		}
		if(flag) puts("Yes");
		else puts("No");
	}
}
