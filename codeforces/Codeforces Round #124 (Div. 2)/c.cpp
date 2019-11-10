#include <bits/stdc++.h>
using namespace std;
const int M = 1e5+10;

char s[M];

int main() {
    scanf("%s", s);
    int la = -1;
    for(int i = 25; i >= 0; i --) {
        for(int j = 0; s[j]; j ++) {
            if(s[j] == i+'a' && j > la) {
                printf("%c", s[j]);
                la = j;
            } 
        } 
    }
    puts("");
}
