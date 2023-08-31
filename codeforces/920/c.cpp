#include <bits/stdc++.h>
const int M = 2e5+10;

int a[M];
char s[M];
std::vector<std::pair<int, int> > ans;

int main() {
	int n; scanf("%d", &n);
	for(int i = 1; i <= n; ++ i) {
		scanf("%d", &a[i]);
	}
	scanf("%s", s+1);
	int l = 1, r = 1;
	for(int i = 1; i <= n; ++ i) {
		if(i > r && l != r) {
			ans.push_back({l, r});
			l = r = i;
		}
		if(a[i] == i) continue;
		if(i <= r && a[i] >= r) {
			r = a[i];
		}
		if(l == r) l = i, r = a[i];
	}
	if(l != r) ans.push_back({l, r});
	bool flag = true;
	for(auto p:ans) {
		for(int i = p.first; i < p.second; i ++) {
			if(s[i] == '0') flag = false;
		}
	}
	if(flag) puts("YES");
	else puts("NO");
}
