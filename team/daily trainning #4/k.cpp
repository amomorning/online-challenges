#include <bits/stdc++.h>
using namespace std;
char s[22], a[22];
int ch[33];
int x[22];
set<string> st;

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n; scanf("%d%s", &n, s);
		memset(ch, 0, sizeof(ch));
		st.clear();
		for(int i = 0; s[i]; ++ i) ch[s[i]-'a'] ++;
		vector<int> mk;
		for(int i = 0; i < 26; ++ i) if(ch[i]&1) mk.push_back(i);
		if(mk.size() > 1) {
			puts("0"); continue;
		}
		int cnt = 0;
		mk.clear();
		for(int i = 0; i < 26; ++ i) {
			for(int j = 0; j < ch[i]/2; ++ j) {
				a[cnt++] = i+'a';
			}
			if(ch[i]/2 > 0) mk.push_back(ch[i]/2);
		}
		a[cnt] = '\0';
		int ans = 1;
		for(int i = 1; i <= cnt; ++ i) {
			ans *= i;
		}
		for(auto tmp:mk) {
			for(int i = 1; i <= tmp; ++ i) {
				ans /= i;
			}
		}
		/*
		for(int i = 0; i < cnt; ++ i) {
			x[i] = i;
		}
		do{
			string s = "";
			for(int i = 0; i < cnt; ++ i) {
				s += a[x[i]];
			}
			// cout << s << endl;
			st.insert(s);
		}while(next_permutation(x, x+cnt));
		printf("%d\n", (int)st.size());
		*/
		printf("%d\n", ans);
	}
}
