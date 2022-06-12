#include <bits/stdc++.h>
const int M = 1e3+10;

int a[M], l[M], r[M];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		std::queue<std::pair<int, int> > q;
		int n; scanf("%d", &n);
		for(int i = 1; i <= n; ++ i) {
			scanf("%d%d", &l[i], &r[i]);
		}
		int cnt = 2;
		q.push({l[1], r[1]});
		int cur = l[1];
		int tot = 1;
		while(cnt <= n) {
			if(l[cnt] != l[cnt-1]) {
				q.push({l[cnt], r[cnt]});
				cnt ++;
			}
			while(cnt <= n && l[cnt] == l[cnt-1]) {
				q.push({l[cnt], r[cnt]});
				cnt ++;
			}
			
			while(!q.empty()) {
				std::pair<int, int> p = q.front(); q.pop();
				// printf("ddd %d %d\n", p.first, p.second);
				if(p.second < cur) a[tot ++] = 0;
				else {
					cur = std::max(cur, p.first);
					a[tot ++] = cur;
					cur ++;
				}
			}
		}
		for(int i = 1; i <= n; ++ i) {
			printf("%d ", a[i]);
		}
	}
}
