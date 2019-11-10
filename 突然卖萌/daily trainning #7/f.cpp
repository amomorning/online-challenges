#include <bits/stdc++.h>
const int N = 1e5+10;

char s[N];
int f[N];
int main() {
	scanf("%s", s+1);
	int n = strlen(s+1);	
	for(int i = 1; i <= n; ++ i) {
		if(s[i] == 'B') f[i] = f[i-1]-1;
		if(s[i] == 'R') f[i] = f[i-1]+1;
	}
	int l = 0, r = 0;
	for(int i = 1; i <= n; ++ i) {
		if(f[i] < f[l]) l = i;
		if(f[i] > f[r]) r = i;
	}
	if(l > r) std::swap(l,r);
	printf("%d %d\n", l+1, r);
}
