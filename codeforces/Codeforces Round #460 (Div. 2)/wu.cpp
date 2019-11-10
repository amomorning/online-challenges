#include <bits/stdc++.h>
std::map<std::string, int> mp;
std::map<std::string, std::string> pre;

void dfs(std::string &s) {
	if(mp[s] == 1) return;
	if(s.length() > 7) return;
	mp[s] = 1;
	std::string t;
	if(s == "WU") {
		t = s;
		std::cout << t << std::endl;
		while(pre[t] != "WJ") {
			t = pre[t];
			std::cout << t << std::endl;
		}
		exit(0);
	}
	if(*s.rbegin() == 'J') {
		t = s+'J';
		// dfs(t);
		if(mp[t] != 1) {
			pre[t] = s;
			dfs(t);
		}
	}
	if(*s.begin() == 'U') {
		t = s + s.substr(1, s.length()-1);
		if(mp[t] != 1) {
			pre[t] = s;
			dfs(t);
		}
	}
	for(size_t i = 2; i < s.length(); ++ i) {
		if(s[i] == s[i-1] && s[i-1] == s[i-2] && s[i] == 'J') {
			// std::cout << s << std::endl;
			t = s.substr(0, i-2) + 'U' + s.substr(i+1, s.length() - i - 1);
			// std::cout << t << std::endl;
			// dfs(t);
			if(mp[t] != 1) {
				pre[t] = s;
				dfs(t);
			}
		}
	}
	for(size_t i = 1; i < s.length(); ++ i) {
		if(s[i] == s[i-1] && s[i] == 'U') {
			// std::cout << s << std::endl;
			t = s.substr(0, i-1) + s.substr(i+1, s.length() - i - 1);
			// std::cout << t << std::endl;
			// dfs(t);
			if(mp[t] != 1) {
				pre[t] = s;
				dfs(t);
			}
		}
	}
}

int main() {
	std::string s = "WJ";
	dfs(s);
	std::string t = "WU";
}
