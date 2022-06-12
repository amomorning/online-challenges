#include <bits/stdc++.h>

int a[55];
int c[1100];
int main() {
	int n; scanf("%d", &n);
	for(int i = 0; i < n; ++ i) {
		scanf("%d", &a[i]);
	}
	std::vector<int> ans;
	for(int i = n-1; i >= 0; -- i) {
		if(c[a[i]]) continue;
		ans.push_back(a[i]);
		c[a[i]] = 1;
	}
	std::reverse(ans.begin(), ans.end());
	printf("%d\n", (int) ans.size());
	for(auto x:ans) {
		printf("%d ", x);
	}
}
