#include <iostream>
#include <cmath>

using namespace std;

int main()
{

    int n, t;
    cin >> t;

    while (t--)
    {
        cin >> n;
        int x = floor(sqrt(n * 2 - 1));
        cout << (x - 1) / 2 << endl;
    }

    return 0;
}