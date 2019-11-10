#include <bits/stdc++.h>

std::map<std::string, std::string> mp;

int main() {
	int n, m;
	scanf("%d%d", &n, &m);
	for(int i = 0; i < n; i ++) {
		std::string name, ip;
		std::cin >> name >> ip;
		mp[ip] = name;
	}
	for(int i = 0; i < m; i ++) {
		std::string name, ip;
		std::cin >> name >> ip;
		ip = ip.substr(0, ip.size()-1);
		std::cout << name << " " << ip << "; #" << mp[ip] << std::endl;
	}
}
