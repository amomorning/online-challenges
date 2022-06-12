#include <bits/stdc++.h>
using namespace std;
const int N = 1e5+10;

int a[N], s[N];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n; scanf("%d", &n);
		for(int i = 0; i < n; ++ i) {
			scanf("%d", &a[i]);
			if(i) s[i] = s[i-1]&a[i];
			else s[i] = a[i];
		}
		int tmp = a[0];
		for(int i = 1; i < n; ++ i) {
			s[i] += s[i-1];
		}
		int ans = s[n-1];
		
		for(int i = 0; i < n; ++ i) {
			ans += (s[n-1]-s[i])&tmp;
			if(i) tmp &= a[i];
		}
		printf("%d\n", ans);
	}
}
