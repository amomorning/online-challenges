#include <bits/stdc++.h>

int v[40];
char mp[40][40];

int main() {
	for(int i = 0; i < 10; ++ i) {
		v[i] = i+'0';
	}
	for(int i = 10; i < 36; ++ i) {
		v[i] = i-10+'A';
	}
	int n; 
	while(~scanf("%d", &n)) {
		for(int i = 0; i < n; ++ i) {
			scanf("%s", mp[i]);
		}
		int now = 0x3f;
		bool flag = true;
		for(int i = 0; i < n; ++ i) now ^= v[i];
		for(int i = 0; i < n; ++ i) {
			int tmp = now;
			for(int j = 0; j < n; ++ j) {
				tmp ^= mp[i][j];
			}
			if(tmp != 0x3f) flag = false;
			tmp = now;
			for(int j = 0; j < n; ++ j) {
				tmp ^= mp[j][i];
			}
			if(tmp != 0x3f) flag = false;
		}
		if(!flag) puts("No");
		else {
			for(int i = 0; i < n; ++ i) {
				if(mp[0][i] != v[i] || mp[i][0] != v[i])  flag = false;
			}
			if(flag) puts("Reduced");
			else puts("Not Reduced");
		}
	}
}
