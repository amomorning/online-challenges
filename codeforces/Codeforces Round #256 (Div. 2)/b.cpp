#include <bits/stdc++.h>
using namespace std;
char s[110], t[110];
int cs[500], ct[500];
multiset<int> ss, tt;

bool judge(int x) {
	int n = strlen(t);
	int m = strlen(s);
	int i = x, j = 0;
	while(i < m && j < n) {
		if(s[i] == t[j]) j ++;
		i ++;
	}
	// printf("%d %d\n", x, j);
	return j == n;
}

int main() {
	scanf("%s%s", s, t);
	if(strlen(t) > strlen(s)) return puts("need tree"), 0;
	for(int i = 0; s[i]; i ++) {
			if(s[i] == t[0] && judge(i)) return puts("automaton"), 0;
	}
	for(int i = 0; s[i]; i ++) {
		ss.insert(s[i]);
		cs[s[i]] ++;
	}
	for(int i = 0; t[i]; i ++) {
		tt.insert(t[i]);
		ct[t[i]] ++;
	}
	if(ss == tt) return puts("array"), 0;
	for(int x:tt) {
		if(ss.find(x) == ss.end()) return puts("need tree"), 0;
		if(cs[x] < ct[x]) return puts("need tree"), 0;
	}
	puts("both");
}

