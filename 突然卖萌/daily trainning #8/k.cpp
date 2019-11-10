#include <bits/stdc++.h>

int a[10];
char mp[5][5];
int tmp[5][5];

int dx[10] = {0, 0, 1, -1, 1, 1, -1, -1};
int dy[10] = {1, -1, 0, 0, 1, -1, 1, -1};

int main() {
	for(int i = 0; i < 3; ++ i) scanf("%s", mp[i]);
	for(int i = 0; i < 9; ++ i) a[i] = i+1;
	int ans = 0;
	do{
		bool g = true;
		for(int i = 0; i < 9; ++ i) {
			int x = i/3, y = i%3;
			if(mp[x][y] != '0' && mp[x][y] != a[i]+'0') {
				g = false;
				break;
			}
			tmp[x][y] = a[i];
		}
		if(!g) continue;
		bool flag = true;
		for(int i = 0; i < 3; ++ i) {
			for(int j = 0; j < 3; ++ j) {
				int t = tmp[i][j];
				int cnt = 0;
				for(int k = 0; k < 8; ++ k) {
					int x = i+dx[k];
					int y = j+dy[k];
					if(x < 0 || y < 0 || x > 2 || y > 2) continue;
					if(tmp[x][y] == t-1 || tmp[x][y] == t+1) cnt ++;
				}
					if(t == 1 || t == 9) {
						if(cnt != 1) flag = false;
					} else {
						if(cnt != 2) flag = false;
					}
			}
		}
		if(flag) ans ++;
	}while(std::next_permutation(a, a+9));
	printf("%d\n", ans);
}
