#include <bits/stdc++.h>
const int M = 1e4+10;
int a[M];

int cnt;
void dfs(int length, int ls,int  now) {
	if(ls == 0) {
		a[cnt ++] = now; 
		return;
	}
	if(length == 1) {
		a[cnt ++] = now + ls;
		return;
	}
	for(int i = 1; i <= ls; i ++) {
		if(i == 10) continue;
		for(int j = 1; j < length; j ++) {
			int tmp = now+i*pow(10, length-1);
			dfs(j, ls-i, now + i*pow(10, length-1));
		}
	}
}

int main() {
	cnt = 0;
	for(int i = 2; i < 9; i ++) {
		dfs(i, 10, 0);
	}
	std::sort(a, a+cnt);
	int n; scanf("%d", &n);
	printf("%d\b", a[n-1]);
}
