#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    cin >> n;
    int path_len = 1;
    long long max_number = n;

    while (n != 1) {
        ++path_len;
        if (n % 2 == 0)
            n /= 2;
        else
            n = 3 * n + 1;
        max_number = max(max_number, n);
    }

    cout << path_len << ' ' << max_number;

    return 0;
}
