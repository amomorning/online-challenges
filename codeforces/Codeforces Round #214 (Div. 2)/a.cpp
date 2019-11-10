#include <bits/stdc++.h>

int main() {
	int n; scanf("%d", &n);
	bool flag = false;
	int l,r,m;
	for(int i = 0; i < 4; ++ i) {
		int a, b, c, d;
		scanf("%d%d%d%d", &a, &b, &c, &d);
		int choco = std::min(a, b);
		int juice = std::min(c, d);
		if(choco + juice > n) continue;
		flag = true;
		m = i+1;
		l = choco;
		r = n-choco;
	}
	if(flag) printf("%d %d %d\n", m, l, r);
	else puts("-1");
}
