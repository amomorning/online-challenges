#include <bits/stdc++.h>
const int inf = 0x3f3f3f3f;
int n, m, i, j, a, b;

int judge(int x, int y) {
	if(x%a != 0) return inf;
	if(y%b != 0) return inf;
	int ta = x/a;
	int tb = y/b;
	if(ta == tb) return ta;
	int d = abs(ta-tb);
	if(d&1) return inf;
	if(ta < tb) {
		if(i-a < 1 && i+a > n) return inf;
	} else {
		if(j-b < 1 && j+b > m) return inf;
	}
	return std::max(ta, tb);
}


int main() {
	scanf("%d%d%d%d%d%d", &n, &m, &i, &j, &a, &b);
	int ans = inf;
	ans = std::min(ans, judge(i-1, j-1));
	ans = std::min(ans, judge(n-i, j-1));
	ans = std::min(ans, judge(i-1, m-j));
	ans = std::min(ans, judge(n-i, m-j));
	if(ans == inf) puts("Poor Inna and pony!");
	else printf("%d\n", ans);
}
