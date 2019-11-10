#include <bits/stdc++.h>
const int N = 1e5+10;
int a[N], b[N];

int main() {
	int n, m; scanf("%d%d", &n, &m);
	for(int i = 0; i < n; ++ i) scanf("%d", &a[i]);
	for(int i = 0; i < m; ++ i) scanf("%d", &b[i]);
	int ta = a[0], tb = 0;
	int j = 0;
	int cnt = 0;
	for(int i = 0; i < n; ) {
		while(ta > tb && j < m) { 
			tb += b[j++];
		}
		if(ta == tb) ta = 0, tb = 0, cnt ++;
		++ i;
		ta += a[i];
	}
	printf("%d\n", cnt);
}
