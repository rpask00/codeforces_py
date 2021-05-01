#include <iostream>
#include <algorithm>

using namespace std;

int main()
{

    int n, t;
    cin >> t;
    while (t--)
    {
        int r = 0;
        cin >> n;
        int arr[100005]{};

        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }

        sort(arr, arr + n);

        for (int i = 1; i < n; i++)
        {
            if (arr[i] > arr[0])
                r++;
        }

        cout << r << endl;
    }
    return 0;
}