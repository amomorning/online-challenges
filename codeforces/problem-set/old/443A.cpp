#include <bits/stdc++.h>

bool ch[300];

int main()
{

    std::string str;
    while (std::cin >> str)
    {
        for (int i = 0; i < str.length(); ++i)
        {
            if (str.at(i) >= 'a' && str.at(i) <= 'z')
            {
                ch[str.at(i)] = true;
            }
        }

    }

    int cnt = 0;
    for(int i = 'a'; i <= 'z'; ++ i) {
        if(ch[i]) cnt ++;
    }
    std::cout << cnt << std::endl;
}
