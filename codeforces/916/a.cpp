#include <bits/stdc++.h>

bool check(int hh, int mm) {
    if(hh == 7 || hh == 17) return false;
    for(int i = 7; i < 60; i += 10) if(mm == i) return false;
    return true;
}

int main() {
    int x;
    int hh, mm;
    scanf("%d%d%d", &x, &hh, &mm);
    int cnt = 0;
    while(check(hh, mm)) {
        mm -= x;
        cnt ++;
        if(mm < 0) hh --, mm += 60;
        if(hh < 0) hh += 24;
    }
    printf("%d\n", cnt);
}
