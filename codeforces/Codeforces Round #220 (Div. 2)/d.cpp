#include <bits/stdc++.h>
#define lson o<<1, l, m
#define rson o<<1|1, m+1, r
const int M = 1e6+10;
int a[M], num[M], T[M<<2];
int q;

void up(int o) { 
	T[o] = T[o<<1] + T[o<<1|1];
}

void update(int o, int l, int r, int v, int p) {
	if(l == r) {
		T[o] = v;
		if(v) num[l] = q;
		return;
	}
	int m = (l+r) >> 1;
	if(p <= (v?m:T[o<<1])) update(lson, v, p);
	else update(rson, v, v?p:p-T[o<<1]);
	up(o);
}

void query(int o, int l, int r) {
	if(T[o] == 0) return;
	if(l == r) {
		printf("%d", num[l]);
		return;
	}
	int m = (l+r) >> 1;
	query(lson);
	query(rson);
}

int main() {
	int n, m;
	scanf("%d%d", &n, &m);
	for(int i = 0; i < m; ++ i) {
		scanf("%d", &a[i]);
	}
	int k = 0;
	for(int i = 0; i < n; ++ i) {
		scanf("%d", &q);
		if(~q) {
			update(1, 1, n, 1, ++k);
		} else {
			// query(1, 1, n); puts("");
			for(int i = 0; i < m; ++ i) {
				// printf("%d\n", T[1]);
				if(T[1] < a[i]-i) break;
				update(1, 1, n, 0, a[i]-i);
			}
			// query(1, 1, n); puts("");
		}
	}
	if(T[1] == 0) puts("Poor stack!");
	else query(1, 1, n);
}
