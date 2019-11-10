#include <bits/stdc++.h>

char a[110][110];

int main() {
	int n; scanf("%d", &n);
	int t = n/2;
	int cnt = 1;
	for(int i = 0; i < n; i ++) {
		for(int j = 0; j < n; j ++) 
			a[i][j] = '*';
		for(int j = t; j < t+cnt; j ++) {
			a[i][j] = 'D';
		}	
		if(i < n/2) {
			t --;
			cnt += 2;
		} else {
			t ++;
			cnt -= 2;
		}
	}
	for(int i = 0; i < n; i ++) printf("%s\n", a[i]);
}
