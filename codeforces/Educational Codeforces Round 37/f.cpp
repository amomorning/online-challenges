#include <bits/stdc++.h>
#define lson o<<1, l, mid
#define rson o<<1|1, mid+1, r
const int M = 3e5+10;
const int N = 1e6+10;

int num[N];
long long T[M<<2], done[M<<2];

void up(int o) {
	T[o] = T[o<<1] + T[o<<1|1];
	done[o] = std::max(done[o<<1], done[o<<1|1]);
}

void build(int o, int l, int r) {
	if(l == r) {
		scanf("%lld", &T[o]);
		done[o] = T[o];
		return;
	}
	int mid = (l+r) >> 1;
	build(lson);
	build(rson);
	up(o);
}

void update(int o, int l, int r, int ql, int qr) {
	if(done[o] <= 2) return;
	if(l == r) {
		T[o] = done[o] = num[T[o]];
		return;
	}
	int mid = (l+r) >> 1;
	if(ql <= mid) update(lson, ql, qr);
	if(qr > mid) update(rson, ql, qr);
	up(o);
}

long long ask(int o, int l, int r, int ql, int qr) {
	if(ql <= l && r <= qr) return T[o];
	long long ret = 0;
	int mid = (l+r) >> 1;
	if(ql <= mid) ret += ask(lson, ql, qr);
	if(qr > mid) ret += ask(rson, ql, qr);
	return ret;
}

int main() {
	for(int i = 1; i < N; ++ i) {
		for(int j = i; j < N; j += i) {
			num[j] ++;
		}
	}
	int n, m; scanf("%d%d", &n, &m);
	build(1, 1, n);
	for(int i = 0; i < m; ++ i) {
		int op, l, r; scanf("%d%d%d", &op, &l, &r);
		if(op==1) update(1, 1, n, l, r);
		else printf("%lld\n", ask(1, 1, n, l ,r));
	}
}
