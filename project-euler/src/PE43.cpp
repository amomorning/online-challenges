#include <bits/stdc++.h>

int main()
{
    // freopen("../data/out.txt", "w", stdout);
    int a[10];
    int b[7] = {2, 3, 5, 7, 11, 13, 17};
    for (int i = 0; i < 10; ++i)
        a[i] = i;
    long long sum = 0;
            // puts("ok");
    do
    {
        bool flag = true;
        for (int i = 0; i < 7; ++i)
        {
            int tmp = 0;
            for (int j = 1; j <= 3; ++j)
            {
                tmp = tmp * 10 + a[i + j];
            }
            if (tmp % b[i] != 0)
            {
                flag = false;
                break;
            }
        }

        if (flag)
        {
            long long tmp = 0;
            for (int i = 0; i < 10; ++i)
                tmp = tmp * 10 + a[i];
            sum += tmp;
            std::cout << sum << std::endl;
        }
    } while (std::next_permutation(a, a + 10));

    int amo; std::cin>>amo;
    return 0;
}