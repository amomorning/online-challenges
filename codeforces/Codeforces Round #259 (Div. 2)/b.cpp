#include <bits/stdc++.h>
const int M = 2e5+10;
int a[M], id[M];

int main() {
	int n; scanf("%d", &n);
	for(int i = 0; i < n; i ++) {
		scanf("%d", &a[i]);
		id[i] = i;
	}
	std::sort(id, id + n, [](int x, int y) {
		return a[x] < a[y];
	});
	bool flag = true;
	for(int i = id[0]; i < n-1; i ++) {
		if(a[i] > a[i+1]) flag = false;
	}
	for(int i = 0; i < id[0]-1; i ++) {
		if(a[i] > a[i+1]) flag = false;	
	}
	if(flag && id[0] == 0) puts("0");
	else if(flag) printf("%d\n", n-id[0]);
	else puts("-1");
}
