#include <bits/stdc++.h>
const int N = 2e5+10;

char s[N];
std::vector<int> a[N];

int main() {
	scanf("%s", s);
	int n = strlen(s);
	int cnt = 0;
	for(int i = 0; s[i]; ++ i) {
		if(s[i] - '0') cnt ++;
	}
	if(cnt >= n - cnt || s[0]-'0') return puts("-1"), 0;
	std::queue<int> q;
	int id = 0;
	int ls = 1;
	bool flag = true;
	std::queue<int> need;
	for(int i = 0; s[i]; ++ i) {
		if(s[i]-'0') {
			if(ls == 1) {
				need.push(id);
				id ++; 
				if(!q.empty()) {
					a[id].push_back(q.front());
					q.pop();
					a[id].push_back(i+1);
					
				} else flag = false;
			} else {
				a[id].push_back(i+1);
			}
			ls = 1;
		} else {
			if(!need.empty()) {
				int idd = need.front();
				need.pop();
				a[idd].push_back(i+1);
				continue;
			}
			if(ls) {
				a[id].push_back(i+1);
				ls = 0;
			}
			else q.push(i+1);
		}
	}
	if(!need.empty() || s[n-1]-'0') flag = false;
	if(flag) {
		printf("%d\n", id+(int)q.size()+1);
		for(int i = 0; i <= id; ++ i) {
			printf("%d", (int)a[i].size());
			for(int x:a[i]) printf(" %d", x);
			puts("");
		}
		while(!q.empty()) {
			printf("1 %d\n", q.front());
			q.pop();
		}
	} else puts("-1");
}
