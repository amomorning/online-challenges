#include <bits/stdc++.h>
const int M = 2e5+10;

char s[M];
std::vector<int> a[M];

int main() {
	scanf("%s", s);
	if(s[0]-'0') return puts("-1"), 0;
	int id = 0;
	std::queue<int> remain;
	std::queue<int> other;
	std::queue<int> need;
	bool flag = true;
	need.push(0);
	int ls = 1;
	for(int i = 0; s[i]; ++ i) {
		if(s[i] - '0') {
			if(ls == 1) {
				if(!remain.empty()) {
					id ++;
					a[id].push_back(remain.front());
					remain.pop();
					a[id].push_back(i+1);
					need.push(id);
				} else if(!other.empty()) {
					a[other.front()].push_back(i+1);
					need.push(other.front());
					other.pop();
				}else flag = false;
			} else {
				a[id].push_back(i+1);
				need.push(id);
			}	
			ls = 1;
		} else {
			if(!need.empty()) {
				a[need.front()].push_back(i+1);
				if(id == need.front()) ls = 0;
				if(id > need.front()) other.push(need.front());
				need.pop();
			}else {
				remain.push(i+1);
			}
		}
	}
	if(!flag || !need.empty()) puts("-1");
	else {
		printf("%d\n", id + (int)remain.size() + 1);
		for(int i = 0; i <= id; ++ i) {
			printf("%d", (int)a[i].size());
			for(int x:a[i]) printf(" %d", x);
			puts("");
		}
		while(!remain.empty()) {
			printf("1 %d\n", remain.front());
			remain.pop();
		}
	}
}
