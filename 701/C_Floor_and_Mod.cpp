#include <iostream>

using namespace std;

int main()
{

    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int a, b, r = 0;
        cin >> a >> b;

        for (int i = 2; i <= b; i++)
        {
            if (i >= a)
                break;

            int mm = i - 1;

            if (a / i <= mm)
            {
                mm = a / i;

                if (a / i > a % i)
                    mm--;
            }

            r += mm;
        }

        cout << r << endl;
    }

    return 0;
}