	#include <bits/stdc++.h>
	using namespace std;
	int main() {
		int n;
		cin >> n;
		vector<pair<int, int> > a(n), b(n);
		for (int i = 0; i < n; i++) {
			cin >> a[i].first;
			a[i].second = i;
		}
		for (int i = 0; i < n; i++) {
			cin >> b[i].first;
			b[i].second = i;
		}
		sort(a.begin(), a.end());                 // 从小到大排序 
		sort(b.begin(), b.end());
		for (int i = 0; i < n; i++) {
			if (a[i].first > b[i].first) {
				cout << "No\n";
				return 0;
			}
		}
		for (int i = 1; i < n; i++) {
			if (a[i] <= b[i - 1]) {
				cout << "Yes\n";
				return 0;
			}
		}
		vector<int> to(n);
		for (int i = 0; i < n; i++) {
			to[a[i].second] = b[i].second;
		}
		int cur = 0;
		int cnt = 0;
		do {
			cur = to[cur];
			cnt++;
		} while (cur != 0);
		cout << (cnt > (n - 1) ? "No\n" : "Yes\n");
		return 0;
	}
