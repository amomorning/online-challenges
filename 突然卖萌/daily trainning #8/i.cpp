#include <bits/stdc++.h>

int t[110][110], a[110];
int main() {
	int n; scanf("%d", &n);
	for(int i = 0; i < n; ++ i) {
		for(int j = 0; j < n; ++ j) {
			scanf("%d", &t[i][j]);
			if(i == j) a[i] = sqrt(t[i][j]);
		}
	}
	for(int i = 0; i < n; ++ i) {
		printf("%d%c", a[i], " \n"[i+1 == n]) ;
	}
}
