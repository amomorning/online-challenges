#include <bits/stdc++.h>
const int M = 1e5+10;
std::vector<int> v[M];

int main() {
	int n, m;
	scanf("%d%d", &n, &m);
	int l = 0;
	int sum = 0;
	for(int i = 1; i <= m; i ++) {
		v[i&-i].push_back(i);
		sum += i&-i;
		l = std::max(l, i&-i);
	}
	if(sum < n) return puts("-1"), 0;
	std::vector<int> ans;
	for(int i = l; i > 0; i >>= 1) {
		for(auto x:v[i]) {
			if(n < i) break;
			n -= i;
			ans.push_back(x);
		}
	}
	printf("%d\n", (int)ans.size());
	for(auto x:ans) printf("%d ", x);
}
