#include <bits/stdc++.h>
#define lson o<<1, l, mid
#define rson o<<1|1, mid+1, r

const int M = 5e5+10;

void up(int o) {
	T[o] = __gcd(T[o<<1], T[o<<1|1]);
}


void build(int o, int l, int r) {
	if(l == r) {
		scanf("%lld", &T[i]);
		return;
	}
	int mid = l+r>>1;
	build(lson);
	build(rson);
	up(o);
}

void update(int o, int l, int r, int p, ll v) {
	if(l == r) {
		T[o] = v;
		return;
	}
	int mid = l+r>>1;
	if(p > m) update(rson, p, v);
	else update(lson, p, v);
	up(o);
}

bool ask(int o, int l, int r, int pl, int pr, ll v) {
	if(pl <= l && r <= pr) {
		
	}
}
