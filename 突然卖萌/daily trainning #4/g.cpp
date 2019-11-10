#include <bits/stdc++.h>
using namespace std;
const int N = 1e6+10;

int a[N], mn[N];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n; scanf("%d", &n);
		for(int i = 0; i < n; ++ i) {
			scanf("%d", &a[i]);
		}
		mn[n] = 0x3f3f3f3f;
		for(int i = n-1; i >= 0; -- i) {
			mn[i] = min(mn[i+1], a[i]);
		}
		int mx = a[0];
		int ans = 0;
		for(int i = 1; i < n-1; ++ i) {
			if(a[i] >= mx && a[i] <= mn[i+1]) {
				ans ++;
			}
			mx = max(mx, a[i]);
		}
		printf("%d\n", ans);
	}
}
