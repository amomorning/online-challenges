#include <bits/stdc++.h>

int main() {
	int n, m;
	scanf("%d%d", &n, &m);
	int sum = 0;
	for(int i = 1; i <= m; i ++) {
		sum += i&(-i);
	}
	if(n > sum) return puts("-1"), 0;
	std::vector<int> ans;
	int l = 1; 
	while(m >= (l<<1)) l <<= 1;
	while(l&-l > n) l >>= 1;
	while(l+2 < n) l += 2;
	for(int i = l; i > 0; i -= 2) {
		if(n < (i&-i)) continue;
		n -= i&-i;
		ans.push_back(i);
	}	
	for(int i = 1; i <= m&&n>0; i += 2) {
		n --;
		ans.push_back(i);
	}
	if(n) return puts("-1"), 0;
	printf("%d\n", ans.size());
	for(auto x:ans) {
		printf("%d ", x);
	}
}
